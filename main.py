from ultralytics import YOLO

# Load a model
model = YOLO("best.pt")  # load a pretrained model (recommended for training)

# Use the model
source = "tiger and elephant.jpg"
results = model(source, save= True)  # predict on an image

# path = model.export(format="ONNX")  # export the model to ONNX format