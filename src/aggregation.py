from .set import fuzzySet

def mamdani(degree, fs: fuzzySet, z):
    return min( degree, fs.func(z))

def larsen(degree, fs: fuzzySet, z):
    return degree * fs.func(z)
