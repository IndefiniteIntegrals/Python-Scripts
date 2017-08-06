# I'm the best yet, and yet, my best is yet to come.

import os
import preprocess


# Resize the images to 256x256 for further preprocessing.
# folders = os.listdir('../data/images')
# for folder in folders:
# 	files = os.listdir('../data/images/{}'.format(folder))
# 	for file in files:
# 		preprocess.resize('{}/{}'.format(folder, file), width=256, height=256)


folders = os.listdir('../new_data/images')
count = 0
for folder in folders:
	files = os.listdir('../new_data/images/{}'.format(folder))
	for file in files:
		if file.endswith('.jpg') or file.endswith('.JPG'):
			preprocess.create_new_samples(folder, file)
			count += 1
			print("Images processed:", count)
