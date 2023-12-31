import torch
import torchvision
import torchvision.transforms as transforms




def get_mean_and_std(loader):
    mean = 0
    std = 0
    total_images_count = 0
    for images, _ in loader:
        image_count_in_a_batch = images.size(0)
        #print(images.shape)
        images = images.view(image_count_in_a_batch, images.size(1),-1)
        mean += images.mean(2).sum(0)
        std += images.std(2).sum(0)
        total_images_count +=image_count_in_a_batch
    
    mean /= total_images_count
    std /= total_images_count

    return mean, std

if __name__=="__main__":
    training_data_path = './images/'
    training_transformation = transforms.Compose([transforms.Resize((224,224)), transforms.ToTensor()])
    train_dataset = torchvision.datasets.ImageFolder(root=training_data_path, transform = training_transformation)
    train_loader = torch.utils.data.DataLoader(dataset = train_dataset, batch_size= 32, shuffle=False)
    print(get_mean_and_std(train_loader))