from roboflow import Roboflow
rf = Roboflow(api_key="uL1f7lU7cprJPcQRYdPi")
project = rf.workspace("roboflow-gw7yv").project("fish-yzfml")
dataset = project.version(44).download("yolov8")
