function [ out ] = Mytemcorr( im, template )
%MYTEMCORR 
%   This function runs template matching with correlation.
%   
%Params
%   im : input image 
%   template : template to be matched in the input image
%
%Notes
%   - Support grayscale only
%   - Code has been refactored for improved performance

tic

% Cast everything into double, matlab loves this!
im = double(im);
template = double(template);

% Get size of image and template
[iy, ix] = size(im);
[ty, tx] = size(template);

% Allocate array for output
out = zeros(iy-ty+1, ix-tx+1);

% Compute static values
t_mean = mean(mean(template));
t_diff = template - t_mean;
t_diff_square_sum = sum(sum( t_diff .^ 2 ));

% Iterate through
for y = 1:iy-ty+1
    for x= 1:ix-tx+1
        
        % extract sub image and calculate its mean
        subim = im(y:y+(ty-1),x:x+(tx-1));
        subim_mean = mean(mean(subim));
        subim_diff = subim - subim_mean;
   
        % calculate upper part               
        upper = sum(sum( subim_diff .* t_diff));
        
        % calculate lower part
        subim_diff_square_sum = sum(sum( subim_diff .^ 2 ));
        lower = sqrt( subim_diff_square_sum * t_diff_square_sum );
        
        out(y,x) = upper / lower;        
        
    end
end

toc

end

