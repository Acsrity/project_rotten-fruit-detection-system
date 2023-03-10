# YOLOV5 for Fresh and Rotten fruits detection
"""

"""

import argparse
import os
import platform
import sys
from pathlib import Path

import torch
from torch.backends import cudnn

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from models.common import DetectMultiBackend
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, loadImgQT, LoadScreenshots, LoadStreams
from utils.general import (LOGGER, Profile, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_boxes, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, smart_inference_mode


class Detect:
    def __init__(self,
                 weights='results/yolo_resnet50.pt'):
        self.weights = weights
        self.bs = 1
        self.save_dir = increment_path(Path(ROOT / 'runs/GUI_Res'), exist_ok=True, mkdir=True)
        self.vid_path = []
        self.vid_writer = []
        self.model = None
        # Load model
        # self.loadModel(weights=weights, imgsz=imgsz)

    def detect(self, imgPath, type=0):
        if (self.model == None):
            self.loadModel()
        if type != 0:
            data = self.loader(imgPath, 1)
        else:
            source = check_file(imgPath)
            data = self.loader(source)
        self.model.warmup(imgsz=(1 if self.pt or self.model.triton else self.bs, 3, *self.imgsz))  # warmup
        seen, windows, dt = 0, [], (Profile(), Profile(), Profile())
        for path, im, im0s, vid_cap, s in data:
            with dt[0]:
                im = torch.from_numpy(im).to(self.model.device)
                im = im.half() if self.model.fp16 else im.float()  # uint8 to fp16/32
                im /= 255  # 0 - 255 to 0.0 - 1.0
                if len(im.shape) == 3:
                    im = im[None]  # expand for batch dim

            # Inference
            with dt[1]:
                # visualize = increment_path(self.save_dir / Path(path).stem, mkdir=True)
                pred = self.model(im, augment=False, visualize=False)

            # NMS
            with dt[2]:
                pred = non_max_suppression(pred, 0.25, 0.45, None, False, max_det=1000)
            # Second-stage classifier (optional)
            # pred = utils.general.apply_classifier(pred, classifier_model, im, im0s)

            # Process predictions
            for i, det in enumerate(pred):  # per image
                seen += 1
                p, im0, frame = path, im0s.copy(), getattr(data, 'frame', 0)

                p = Path(p)  # to Path
                save_path = str(self.save_dir / p.name)  # im.jpg
                s += '%gx%g ' % im.shape[2:]  # print string
                annotator = Annotator(im0, line_width=3, example=str(self.names))
                if len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0.shape).round()
                    res = ''
                    # Print results
                    for c in det[:, 5].unique():
                        n = (det[:, 5] == c).sum()  # detections per class
                        s += f"{n} {self.names[int(c)]}{'s' * (n > 1)}, "  # add to string
                        res = self.names[int(c)]
                    # Write results
                    for *xyxy, conf, cls in reversed(det):
                        c = int(cls)  # integer class
                        label = None if False else (self.names[c] if False else f'{self.names[c]} {conf:.2f}')
                        annotator.box_label(xyxy, label, color=colors(c, True))

                # Stream results
                im0 = annotator.result()

                if (type != 0):
                    return im0

                # Save results (image with detections)
                if data.mode == 'image':
                    cv2.imwrite(save_path, im0)
                else:  # 'video' or 'stream'
                    if self.vid_path[i] != save_path:  # new video
                        self.vid_path[i] = save_path
                        if isinstance(self.vid_writer[i], cv2.VideoWriter):
                            self.vid_writer[i].release()  # release previous video writer
                        if vid_cap:  # video
                            fps = vid_cap.get(cv2.CAP_PROP_FPS)
                            w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                            h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        else:  # stream
                            fps, w, h = 30, im0.shape[1], im0.shape[0]
                        save_path = str(Path(save_path).with_suffix('.mp4'))  # force *.mp4 suffix on results videos
                        self.vid_writer[i] = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
                    self.vid_writer[i].write(im0)

            # Print time (inference-only)
            LOGGER.info(f"{s}{'' if len(det) else '(no detections), '}{dt[1].dt * 1E3:.1f}ms")
        return im0, res

    def loader(self, source, type=0):
        if type == 0:
            dataset = LoadImages(source, img_size=self.imgsz, stride=self.stride, auto=self.pt, vid_stride=1)
        else:
            dataset = loadImgQT('', source, img_size=self.imgsz, stride=self.stride, auto=self.pt, vid_stride=1)
        self.vid_path, self.vid_writer = [None] * self.bs, [None] * self.bs
        return dataset

    def loadModel(self, weights='results/yolo_resnet50.pt', imgsz=(640, 640)):
        weights = ROOT / weights
        self.weights = weights
        self.model = DetectMultiBackend(weights=weights, device=select_device('0'), dnn=False, fp16=False)
        self.stride, self.names, self.pt = self.model.stride, self.model.names, self.model.pt
        self.imgsz = check_img_size(imgsz, s=self.stride)  # check image size
        print('load model successfully')
