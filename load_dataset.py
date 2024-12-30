import pickle5 as pickle

with open('../measurements 2018_04.pickle', 'rb') as file:
    dataset = pickle.load(file)

print('excitation signal', dataset['excitation signal'].shape)
"""
    the signal for exciting a guided wave
    1000 values (all guided waves are generated using the same excitation signal,
    which consists of 1000 samples and lasts for 1 millisecond)
"""
print('guided wave', dataset['guided wave'].shape)
"""
    measured guided wave
    14994x8x2000 values (14994 measurements,Each measurement collects 8 guided waves, 
    with each wave consisting of 2000 samples. The first through eighth guided waves, 
    among the 8 collected correspond to paths 5-1,5-2,5-3,5-4,6-16-2, 6-3 and 6-4, respectively.)
"""
print('datatime', dataset['datatime'].shape)
"""
    measurement time
    14994 values (each measurement records time once)
"""
print('temperature', dataset['temperature'].shape)
"""
    measured environment temperature
    14994 values (each measurement records temperature once)
"""
print('humidity', dataset['humidity'].shape)
"""
    measured environment humidity
    14994 values (each measurement records humidity once)
"""
print('brightness', dataset['brightness'].shape)
"""
    measured environment brightness
    14994 values (each measurement records brightness once)
"""
print('pressure', dataset['pressure'].shape)
"""
    measured environment pressure
    14994 values (each measurement records air pressure once)
"""
print('damage tag', dataset['damage tag'].shape)
"""
    damage type for each measurement
    14994 values (damage tag ranges from 0 to 13 where 0 represents "healthy status" and 1 to 13 
    indicate the corresponding damage types from 1 to 13)
"""
print('weather tag', dataset['weather tag'].shape)
"""
    weather type for each measurement
    14994 values (weather tag ranges from 0 to 5,with 0 representing "fair weather" and 1 to 5 
    corresponding to "precipitation","light rain", "rain","snow", and "mixed weather" respectively.)
"""
print('data inf', "("+str(len(dataset['data inf']))+",)")
"""
    providing an explanation for all the keys in this file
    9 keys and values (including excitation signal, guided wave, datatime, temperature,humidity, 
    brightness, pressure, damage tag and weather tag.)
"""
