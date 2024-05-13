import numpy as np

# 예시를 위해 임의로 무작위이미지 생성
img = np.random.rand(8,8,3)

#############################################################
##                      pixel 2 patch                      ##
#############################################################
# Step 1. 이미지를 (2, 4, 2, 4, 3) 로 reshape (4X4가 하나의 patch)
img = img.reshape(2,4,2,4,3)

# Step 2. 각 patch가 독립된 차원을 갖도록 재배열
img = img.transpose(0, 2, 1, 3, 4)

# Step 3. 이제 patch = (4,4,3)크기 배열.
patches = img.reshape(-1, 4, 4, 3)

print(patches.shape) # output:(4,4,4,3)



##########################################################################
#     patch 2 vector (32차원 embedding 공간으로 linear projection)          #   
#     기존 patch는 4X4X3 = 48차원으로 embedding을 위해 먼저 1차원으로 펼쳐야 함     #
# 이후 embedding과정을 거친 이후 embedding 차원으로 1차원으로 펼친 patches를 투영시킴 #
#########################################################################
import torch
import torch.nn as nn

# Flatten to 1D Vector
flatten_patches = patches.reshape(patches.shape[0], -1)

# Pytorch Tensor로 변환
flatten_patches_tensor = torch.Tensor(flatten_patcehs)

# embedding 차원 설정.
embedding_dim = 32

# 선형투영할 FC Layer 정의
fc = nn.Linear(flatten_patches_tensor.shape[-1], embedding_dim)

# Linear Projection 실행
projected_patches = fc(flatten_patches_tensor)

print(projected_patches.shape) # output: torch.Size([4, 32])
