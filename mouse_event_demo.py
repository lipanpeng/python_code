## Mouse event demo

import cv2
import glob
import os
import imageio

data_dir = r'D:\Li_Panpeng\projects\data\AF\move3'
crop_width = 384
crop_height = 384
def main():
    img_list = glob.glob(os.path.join(data_dir, 'img_0', '*.png'))
    object_depth = open(os.path.join(data_dir, 'object_depth.txt'), 'w')
    object_depth.write('img_name x y depth\n')

    def get_depth(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(x, y)
            print(param[0][y][x])
            cv2.destroyAllWindows()
            object_depth.write('{} {} {} {}\n'.format(param[1], x, y, param[0][y][x]))


    def crop_img(event, x, y, flags, param):
        crop_folder = os.path.join(data_dir, 'img_0', 'defocus', 'crop')
        if not os.path.exists(crop_folder):
            os.mkdir(crop_folder)
        index = param[0]
        if event == cv2.EVENT_LBUTTONDOWN:
            for i in range(51):
                img_name = index + '_{:0>4d}.png'.format(i)
                crop_img_name = index + '_{:0>4d}_crop.png'.format(i)
                img = cv2.imread(os.path.join(data_dir, 'img_0', 'defocus', img_name))
                # cv2.imshow('test', img[int(y-crop_height/2): int(y+crop_height/2)][int(x-crop_width/2): int(x+crop_width/2)][:])
                img_crop = img[int(y-crop_height/2): int(y+crop_height/2), int(x-crop_width/2): int(x+crop_width/2), :]
                cv2.imwrite(os.path.join(crop_folder, crop_img_name), img_crop)
            cv2.destroyAllWindows()



    for i in img_list:
        img = cv2.imread(i)
        print(type(img))
        index = i.split('\\')[-1].split('.')[0].split('_')[-1]
        print(i, index)
        pfm_name = 'img_1_' + index + '.pfm'
        pfm = imageio.imread(os.path.join(data_dir, 'img_1', pfm_name))
        cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        cv2.imshow('img', img)
        cv2.setMouseCallback('img', get_depth, [pfm, i])
        cv2.waitKey(0)

    object_depth.close()

if __name__ == "__main__":
    main()

