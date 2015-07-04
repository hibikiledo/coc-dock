function [ res ] = locateres( imfname, templatefname, outputfname )
%LOCATERESOURCES Summary of this function goes here
%   Detailed explanation goes here

% Read in preprocessed image
im = imread( imfname );

% Read in template
template = imread( templatefname );

% Get template size
[ty, tx] = size(template);

% Find matches of template in scene
res = Mytemcorr(im, template);

% Filter with threshold = 0.85
[rows,cols] = find(res > 0.85);

% Since rows and cols are noe mapped to top-left
% we need to adjust the value to center
% we multiplied 2 since the original image is scaled down by 0.5
rows = (rows + round((ty/2))) * 5;
cols = (cols + round((tx/2))) * 5;

% Get size of r and c
rr = size(rows);
cc = size(cols);

% Write result into file
fileID = fopen(outputfname, 'w');

% Print output to file
for i = 1:rr
    fprintf(fileID, '%d:%d\n', cols(i), rows(i));
end

% Close file 
fclose(fileID);

% Terminate matlab
exit;

end

