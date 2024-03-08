import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    nums = np.array(list)
    flat = nums.copy()
    nums = nums.reshape(3,3)
    calculations = {'mean': [np.mean(nums,axis = 0).tolist(), np.mean(nums,axis = 1).tolist(), np.mean(flat)],
                    'variance': [np.var(nums,axis = 0).tolist(), np.var(nums,axis=1).tolist(), np.var(flat)],
                    'standard deviation': [np.std(nums,axis=0).tolist(), np.std(nums,axis=1).tolist(), np.std(flat)],
                    'max': [np.max(nums,0).tolist(), np.max(nums,1).tolist(), np.max(flat)],
                    'min': [np.min(nums,0).tolist(), np.min(nums,1).tolist(), np.min(flat)],
                    'sum': [np.sum(nums,0).tolist(), np.sum(nums,1).tolist(), np.sum(flat)]}
    


    return calculations