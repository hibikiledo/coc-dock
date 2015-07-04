function [out] = preprocess(infname, outfname)

% Read in image
im = imread(infname);

% Rotate
im = imrotate(im, 90);

% Down sampling
im = imresize(im, 0.2);

% Convert into grayscale
out = rgb2gray(im);

% Save
imwrite(out, outfname);

% Terminate matlab process
exit;