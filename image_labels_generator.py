import boto3

def init_rekognition_client():
    return boto3.client('rekognition', region_name='ap-south-1')  # Ensure the region is correct

def detect_labels(image_bytes):
    client = init_rekognition_client()
    response = client.detect_labels(
        Image={'Bytes': image_bytes},
        MaxLabels=10,
        MinConfidence=75
    )
    return response['Labels']

def load_image(image_path):
    with open(image_path, 'rb') as image_file:
        return image_file.read()

def process_image(image_path):
    try:
        image_bytes = load_image(image_path)
        labels = detect_labels(image_bytes)
        print(f"\nLabels for {image_path}:")
        for label in labels:
            print(f"  Label: {label['Name']}, Confidence: {label['Confidence']:.2f}%")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def main(image_paths):
    for image_path in image_paths:
        process_image(image_path)

if __name__ == "__main__":
    image_paths = [
        'C:/Users/shivt/Downloads/cat img.jpg',
        'C:/Users/shivt/Downloads/chicken image.jpg',
        # Add more image paths as needed
    ]
    main(image_paths)
