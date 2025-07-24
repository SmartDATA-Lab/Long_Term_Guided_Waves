# Open Guided Waves

This GitHub repository is created in support of the paper **"Open Guided Waves: Long-Term Guided Wave Based Structural Health Monitoring under Uncontrolled and Highly Dynamic Conditions"**. You can access the full article [here](https://doi.org/10.1038/s41597-025-05300-5).  
This repository provides an introduction to the **Open Guided Waves**. We provide a long-term, real-world structural health monitoring (SHM) benchmark dataset to support damage detection and analysis under varying environmental conditions.

## Abstract
Few studies address guided wave structural health monitoring under controlled and dynamic environments, largely due to the lack of a public benchmark dataset. To address this gap, this paper presents a public dataset from a long-term outdoor structural monitoring experiment conducted at the University of Utah, Salt Lake City. The monitoring, spanning over 4.5 years, collected approximately 6.4 million guided waves under both regular environmental variations (e.g., daily temperature changes ranging from 260.95 K (−12.2 °C) to 325.65 K (52.5 °C)) and irregular variations (e.g., rain and snow). The measured guided waves in the public dataset are also affected by sensor drift and installation shifts consistently over time. Additionally, thirteen types of damage were introduced to the monitored structure to support damage detection and severity evaluation under these conditions. The dataset includes measurement times, temperature, humidity, air pressure, brightness, and weather information to aid in damage detection. The provided public dataset aims to assist researchers in developing more practical methods for structural health monitoring in uncontrolled and dynamic environments.

## Background & Summary
To address the need of public benchmark data for evaluating the effectiveness of damage detection methods in practical environmental and operational conditions, this work presents a public benchmark dataset gathered from a long-term outdoor guided wave structural health monitoring experiment conducted under uncontrolled and dynamic conditions. The dataset was collected in outdoor environments at the University of Utah, Salt Lake City, between March 2018 and October 2022, amassing approximately 6.4 million guided wave data points under various environmental conditions. The dataset also includes corresponding measurements of surrounding environmental factors such as temperature, humidity, brightness, air pressure, and weather information during the guided wave collection process. A total of 13 different types of damage were introduced, ranging from minor to severe, including metal mass attachments, small dents, and through-hole damage. Detailed descriptions of the data acquisition equipment, collection processes, and damage generation methods are provided in this paper. Challenges in long-term structural health monitoring under uncontrolled and dynamic environmental conditions—including regular and irregular environmental variations, sensor drift, installation drift, and variations in damage severity—are demonstrated using correlation coefficients between adjacent guided waves and optimal correlation coefficients between guided waves and their baseline guided waves, based on the public benchmark dataset. The results show that certain regular and irregular environmental variations, sensor drift, and installation drift can distort guided waves more significantly than structural damage itself. Overall, this public dataset makes four key contributions to the structural health monitoring community:

1. **Public Dataset for Real-World SHM Evaluation**: We provide the first publicly available benchmark dataset specifically created to assess the effectiveness of guided wave-based methods for long-term structural health monitoring in uncontrolled and dynamic outdoor environments.

2. **Identification of Key Challenges**: The dataset highlights four primary challenges in the public dataset: regular (e.g., daily changes in temperature and humidity) and irregular environmental conditions (e.g., rain and snow), sensor drift, installation drift, and damage severity variation. These challenges will motivate researchers to develop more practical and robust damage detection techniques suitable for real-world outdoor monitoring.

3. **Comprehensive Damage Types**: We introduce 13 types of damage with gradually increasing severity, ranging from small dents to large through-hole damage. This enables the dataset to be used for evaluating the effectiveness of guided wave-based methods in assessing damage severity under uncontrolled, dynamic outdoor conditions.

4. **Large-Scale Measurement Collection**: The dataset includes measurements taken approximately every 170 seconds, with each measurement consisting of 8 guided waves (transmitted by 2 actuators and received by 4 sensors). The extensive data from various sensors facilitates research into data fusion. Over 4.5 years, the dataset contains about 6.4 million measurements, providing a rich benchmark for testing guided wave compression techniques and evaluating the efficiency of damage detection methods using fewer measurements.
## Methods
We developed a structural health monitoring system at the University of Utah in Salt Lake City to implement and investigate
long-term monitoring under uncontrolled and dynamic conditions. The monitored structure was initially an intact aluminum
plate of 53 cm x 53 cm x 3 mm. This plate was placed on the first layer of the shelf, as illustrated in part (a) of Fig. 1.The monitored plate was placed on the first layer of a
shelf, as shown in part (a) of Fig. 2. To generate and receive guided waves, we transmitted a 1 ms linear chirp with a center
frequency ranging from 5 kHz to 350 kHz using sensors 5 and 6. Each response was recorded at a sampling rate of 1 MHz.
Measurements were taken approximately every 8.6 seconds, with only the first 10, 000 samples (10 ms) recorded for each
guided wave, as shown in part (a) of Fig. 3. Details of the sensors and data acquisition system are provided in Table.1

![Overview of the Monitoring Setup](/figures/Fig1.png)
*Figure 1. The actual positions of the lead zirconate titanate (PZT) transmitters (sensors 5 and 6) and receivers (sensors 1, 2, 3 and 4) are displayed in the left figure, while the precise coordinates (X: cm, Y: cm) are provided in the right figure.*  

![ExpSetup](/figures/Fig2.png)
*Figure 2. Figure (a) shows the monitored structure, an aluminum plate, positioned on the first layer of a shelf. The data acquisition
system was housed in a foam box on the second layer of the shelf. Figures (b) and (c) display the locations of the temperature,
brightness, air pressure, and humidity sensors, which were mounted on the exterior of the foam box.*

![Raw Signal](/figures/Fig3.png)
*Figure 3. The original guided wave, consisting of 10,000 samples and lasting 10 ms. This guided wave was collected from path 5-4 at 20:18:06 on April
24, 2021, at a measurement temperature of 16.57 ◦ C.*

![Table 1](/figures/Table1.png)
*Table 1. Information of environmental sensors and DAQ system.*

## 0.1 Long-term Monitoring Under Uncontrolled and Dynamic Conditions

The monitored structure (an aluminum plate), along with the sensors and data acquisition systems, were placed in a small room
with four walls but no roof at the University of Utah, Salt Lake City, as illustrated in part (a) of Fig. 2. This setup exposed
the monitored structure and the structural health monitoring system to the outdoor environment under natural and dynamic
conditions. The monitored structure and guided wave sensors endured various harsh environmental conditions, as depicted in
Fig. 4. 

![Fig 4](/figures/Fig4.png)
*Figure 4. During long-term monitoring, the monitored plate and the structural health monitoring system were exposed to
various weather conditions, including rain, icing, and snow, as shown in Figures (a), (b), and (c), respectively.*

## 0.2 Damage Generation and Damage Type Information
Starting on April 17th, 2021, we introduced 13 types of damage to the monitored structure. Detailed information about the
damage can be found in Table 2, and the damage positions and shapes are illustrated in Fig. 5. In total, 13 types of damage
were generated, labeled from "D1" to "D13", with the severity of the damage increasing progressively. This dataset can serve as
a benchmark for evaluating the performance of guided wave-based structural health monitoring method in identifying damage
and assessing damage severity.

![Fig 5](/figures/Fig5.png)
*Figure 5. Six types of damage were created sequentially on the center of the same aluminum plate from April 17, 2021 to
September 19, 2021.*

![Table 2](/figures/Table2.png)
*Table 2. Description about the 13 types of damage on the aluminum plate.*

## 1 Data Records
The dataset is available at the repository titled “Dataset on Guided Waves from Long-Term Structural Health Monitoring under Uncontrolled and Dynamic Conditions” on figshare. In the repository,approximately five years of monitoring data are stored in 56 ".pickle" files. Each file is named in the format "measurements
year_month.pickle," where the numbers in the filename represent the year and month of the measurements it contains. For
example, measurements from April 2018 are stored in "measurements 2018_04.pickle". These files are publicly ac-
cessible through the provided website link (https://doi.org/10.6084/m9.figshare.28112504). Each ".pickle" file is a dictionary with 10 keys, as shown in Table 3. The key "guided wave" contains 8
channels of ultrasonic guided waves. In the "measurements 2018_04.pickle" file, for example, the "guided wave"
matrix has dimensions of 14, 997 × 8 × 2000, representing 14, 997 measurements with each measurement including 8 channels
of guided waves from paths 5-1, 5-2, 5-3, 5-4, 6-1, 6-2, 6-3, and 6-4. Each guided wave comprises 2000 samples and lasts
2 ms. The keys "datetime", "temperature", "humidity", "brightness", and "air pressure" record the measurement time and
the corresponding environmental conditions (temperature, humidity, brightness, and air pressure) at the time of guided wave
measurement. The key "damage tag" provides damage information for each measurement, with a value of 0 indicating no
damage and values from 1 to 13 denoting damage types from "D1" to "D13", as shown in Table 2. Additionally, the key
"weather tag" records the weather conditions from public weather website during each measurement, ranging from 0 to 5,
with 0 representing "fair weather" and 1 to 5 corresponding to "precipitation," "light rain," "rain," "snow," and "mixed weather,"
respectively. Note that the 15-mile distance between the meteorological station and the experiment location may introduce some imprecision in the weather records. The key information ("guided wave", "datetime", "temperature", "humidity", "brightness", "air pressure", "damage tag", and "weather tag") for each measurement file is explained under the "data inf" key within each file.

# Technical Validation
The study leverages correlation coefficients between adjacent guided waves, as well as optimal correlation coefficients with baseline guided waves, to validate structural health challenges present in the public dataset—challenges that are also common in practical structural health monitoring under uncontrolled and highly dynamic conditions. This technical validation helps researchers recognize the characteristics and challenges of guided waves obtained from real-world dynamic environments, aiding in the development of effective methods for practical structural health monitoring.

1. **Challenge 1**: Both regular and irregular environmental variations alter guided waves, with irregular variations like rain and snow sometimes causing greater impact than through-hole damage.

2. **Challenge 2**: Sensor drift over time can create differences in guided waves even under similar environmental conditions, complicating baseline comparisons and data-driven-based damage detection.

3. **Challenge 3**: Installation shifts, occurring during repairs or updates to the monitoring system, can lead to differences in guided waves, affecting baseline comparisons and data-driven-based 
damage detection.

4. **Challenge 4**: Certain types of damage may not significantly alter guided waves, making detection difficult.

## 1.1 Validation (Challenge) 1: Distortion of Guided Waves Due to Environmental Variations
In the long-term uncontrolled structural health monitoring, the temperature varied from 260.95 K (−12.2 °C) to 325.65 K (52.5 °C), while humidity ranged from 0.5% to 146.3%. Theoretically, the maximum humidity value is 100%, and values exceeding 100%, such as 146.2%, occurred during precipitation events and resulted from improper calibration. Brightness was measured in lux, with values ranging from 0.0003 to 3615537.4. Air pressure varied from 867.2 hPa to 1335.3 hPa. Environmental variations can be classified into regular and irregular categories based on their frequency of occurrence. Regular environmental variations, such as daily changes in temperature and humidity, are consistent and prevalent throughout long-term monitoring. In contrast, irregular environmental variations, such as rain and snow, occur less frequently. Typically, regular environmental variations change gradually, while irregular variations fluctuate rapidly and dramatically. For instance, daily temperature changes are usually less than 2 °C per hour and relatively stable. However, during irregular environmental conditions, like rain or direct sunlight, temperature changes can be much more rapid and drastic, sometimes exceeding 10 °C per hour, as shown in part (b) of Fig. 6. The impact of both regular and irregular environmental variations on guided wave distortion is illustrated by changes in the (Pearson) correlation coefficient between adjacent guided waves, as shown in Fig. 6 and Fig. 7 and between guided waves and their optimal baseline (referred to as optimal correlation coefficients), as depicted in Fig. 9.
## 1.2 Validation (Challenge) 2: Distortion of Guided Waves Due to Sensor Drift
Figure 9 demonstrates sensor drift by presenting the optimal correlation coefficients for guided waves from paths 5-1, 5-2, 6-1, and 6-2, marked as “Sensor Drift.” The baseline guided waves were collected in July 2019, and the optimal correlation coefficient for each path (e.g., 5-1) is calculated by comparing the guided waves from the corresponding baselines collected from the same path, using Algorithm 1. As seen in Fig. 9, the optimal correlation coefficients peak around July each year. However, while the coefficients for July 2019 approach 1, those for July in subsequent years, like 2020 and 2021, do not, even under similar environmental conditions. This decline is more noticeable for guided waves collected more later, indicating sensor drift. Additionally, sensor drift severity varies across sensors; for example, guided waves from path 6-1 in July 2020 and 2021 show optimal correlation coefficients closer to 1 compared to paths 5-1, 5-2, and 6-2. Sensor drift is a common issue in long-term monitoring, potentially leading to false alarms if not properly addressed through updated baseline datasets, training data, or drift compensation methods. Our public dataset provides a benchmark for evaluating the effectiveness of methods designed to detect damage in the presence of sensor drift, detect sensor drift, or compensate guided waves for sensor drift.

## 1.3 Validation (Challenge) 3: Distortion of Guided Waves Due to Installation Shift

Another challenge is the occurrence of installation shifts during long-term structural health monitoring. Sensors, coupling layers, and data acquisition systems often require repair or updates over time. During the reinstallation of these components, installation shifts may occur. In other words, replaced sensors, coupling layers, or data acquisition and sampling systems may differ from the original ones. Additionally, their positions, such as those of PZT and environmental sensors, may not be exactly the same as before. Consequently, these installation shifts can result in collected guided waves differing from previous ones, even if the environmental and operational conditions remain unchanged . In our long-term monitoring system, we updated brightness and air pressure sensors in September 2018. During this reinstallation, we unintentionally altered the environmental setup and sensor positions, leading to guided waves collected after September being markedly different from those collected earlier. This is illustrated in Fig.9, where the optimal correlation coefficients for 2018 are close to 0, even for guided waves collected in July 2018, which had similar environmental conditions to the baseline measurements from July 2019.  To address this challenge, researchers and engineers should ensure that the same equipment is used and positioned consistently during system updates. Additionally, methods to detect installation shifts under complex and dynamic conditions should be developed, along with compensation techniques to update baselines or training data to mitigate the effects of installation shifts.

![Fig 6](/figures/Fig6.png)
*Figure 6. The first two subplots in parts (a) and (b) show the correlation coefficients between two adjacent guided waves
collected from paths 5-1 and 5-2. The corresponding time and humidity are depicted in the third and fourth subplots.*
![Fig 7](/figures/Fig7.png)
*Figure 7. This figure presents results similar to those in Fig. 6, but using guided waves from paths 5-1 and 5-2 collected at
different times.*
![Fig 8](/figures/Fig8.png)
*Figure 8. The blue curve in each of the four subplots represents guided waves collected from path 5-4 under different
conditions: rain, freezing temperatures, direct sunlight, and through-hole damage, as indicated in the title of each subplot. The
measurement time and temperature are labeled in the legend of each subplot. The background guided wave, marked with gray
color, shown for comparison, was collected under fair weather conditions, as depicted in Fig. 3.*
![Fig 9](/figures/Fig9.png)
*Figure 9. The first four subplots display the optimal correlation coefficients for guided waves collected from paths 5-1, 5-2,
6-1, and 6-2, respectively. The baseline guided waves were collected in July 2019. The corresponding temperature and
humidity measurements are shown in the fifth and sixth subplots.*

## 1.4 Validation (Challenge) 4: Distortion of Guided Waves Due to Damage Severity Variation

Figs. 10 to 16 show the optimal correlation coefficients for guided waves collected from the same monitored structure with various types of damage. Each subplot displays 10 days of test data, with five days before and after the introduction of new damage, highlighted in gray. The baseline guided waves for each dataset were collected during the 10 days preceding the test data. For example, in part (a) of Fig. 10, the test guided waves span from April 13th to April 22nd, 2021, covering five days of healthy conditions and five days with damage "D1". The baseline guided waves were collected from April 4th to April 13th.2021. Conversely, part (b) of Fig. 10 illustrates test guided waves from May 13th to May 22nd, 2021, including five days of
healthy conditions and five days with damage "D2", with the baseline collected from May 4th to May 13th, 2021. Each figure’s
first four subplots show the optimal correlation coefficients for paths 5-1, 5-2, 5-3, 5-4, 6-1, 6-2, 6-3, and 6-4, using baseline
guided waves from the corresponding sensor paths.
For damage D-1, a notable drop in optimal correlation coefficients was observed for guided waves from paths 6-1, 6-2, 6-3,
and 6-4, but not from paths 5-1, 5-2, 5-3, and 5-4. This decline could be due to rain around April 15th, which also caused a
coefficient drop, as seen in part (a) of Fig. 10. No significant decline was noted when detecting damage "D2" from healthy
conditions or damage "D3" from damage "D2", possibly because the dents were too minor to significantly impact the guided
waves, as illustrated in part (b) of Fig. 10 and part (a) of Fig. 11. In contrast, for damage "D4" and "D5", a slight decline in
optimal correlation coefficients was observed, suggesting that these dents were deep enough to significantly affect the guided
waves, as shown in part (b) of Fig. 11 and part (a) of Fig. 12. Larger dents from damage "D6" and damage "D7" resulted in a
more noticeable decline, as shown in part (b) of Fig. 12 and part (a) of Fig. 13. However, the overall decline in coefficients for
damage "D3" to "D7" was minor.
When through-hole damage (from "D8" to "D13") was introduced, a more significant decline in optimal correlation
coefficients was observed, indicating that these damages had a more substantial impact on the monitored structure, as depicted
in Figs. 13 to 16. However, irregular environmental variations, such as rain, caused an even more pronounced decline in
coefficients compared to through-hole damages, as shown in Figs. 15 and 16. Therefore, accurate detection of environmental
variations is crucial to minimize false alarms.

## 1.5 Validation (Challenge) 5: Damage Localization with this Public Dataset
Theoretically, the public benchmark dataset can be used to evaluate methods for damage localization under complex and dynamic
conditions, as each measurement collects 8 ultrasonic guided waves from 4 different receivers and 2 different transmitters. By
analyzing the arrival time differences of signals induced by damage, the damage location can be determined. However,
isolating damage-induced signals in this dataset is challenging due to multiple guided wave reflections from the edge of
the monitored structure for two main reasons. First, the excitation signal duration is relatively long, lasting 1 ms, whereas
the monitored structure is relatively small, measuring only 53 cm × 53 cm × 3 mm. Given that the guided wave speed is
approximately 3 to 6 km/s, the time for guided waves to travel from one point to another on the plate is less than 0.2 ms,
which is shorter than the duration of the chirp excitation signal (1 ms). Second, the positions of the guided wave receivers
were very close to the plate’s edge. Consequently, before the end of the excitation signal, receivers will have already picked up
multiple reflections from the plate’s edge. As illustrated in parts (a) and (b) of Fig. 3, determining the first arrival of guided
waves, which is typically used to separate damage-induced signals for damage localization, is challenging. We also applied
pulse compression to the guided waves using the excitation signal, a common method to locate the first arrival time by finding
the peak value of the correlation coefficient between the excitation signal and the guided wave samples. The first arrival
time for guided waves collected from path 5-4 should be less than 0.1 ms. However, the peak value for pulse-compressed
guided waves from path 5-4 occurs around 0.2 ms, as shown in part (c) of Fig.3. This delay in the peak value may be caused by
reflected guided waves. In summary, while the public dataset can theoretically be used for damage localization, the challenges
in separating the first arrival of guided waves from damage-induced waves require further investigation .

![Fig 10](/figures/Fig10.png)
*Figure 10. The first four subplots in Part (a) and (b) illustrate the optimal correlation coefficients for measurements from paths
5-1, 5-2, 5-3, 5-4, 6-1, 6-2, 6-3, and 6-4. The corresponding measured temperature and humidity are shown in the fifth and
sixth subplots. The shadow regions in part(a) and part (b) indicates that the measurements collected from healthy structure to
the structure with damage D1, and to damage D2, respectively.*

![Fig 11](/figures/Fig11.png)
*Figure 11. These subplots illustrate the same contents as those in Fig. 10. The shadow regions in parts (a) and (b) indicate
measurements collected from the structure with damage D2 to the structure with damage D3, and the structure with damage D3
to the structure with damage D4, respectively.*

![Fig 12](/figures/Fig12.png)
*Figure 12. These subplots illustrate the same contents as those in Fig. 10. The shadow regions in parts (a) and (b) indicate
measurements collected from the structure with damage D4 to the structure with damage D5, and the structure with damage D5
to the structure with damage D6, respectively.*

![Fig 13](/figures/Fig13.png)
*Figure 13. These subplots illustrate the same contents as those in Fig. 10. The shadow regions in parts (a) and (b) indicate
measurements collected from the structure with damage D6 to the structure with damage D7, and the structure with damage D7
to the structure with damage D8, respectively.*

![Fig 14](/figures/Fig14.png)
*Figure 14. These subplots illustrate the same contents as those in Fig. 10. The shadow regions in parts (a) and (b) indicate
measurements collected from the structure with damage D8 to the structure with damage D9, and the structure with damage D9
to the structure with damage D10, respectively.*

![Fig 15](/figures/Fig15.png)
*Figure 15. These subplots illustrate the same contents as those in Fig. 10. The shadow regions in parts (a) and (b) indicate
measurements collected from the structure with damage D10 to the structure with damage D11, and the structure with damage
D11 to the structure with damage type D12, respectively.*

![Fig 16](/figures/Fig16.png)  
*Figure 16. These subplots illustrate the same contents as those in Fig. 10. The shadow regions indicate measurements
collected from the structure with damage D12 to the structure with damage D13.*

# Citing Open Guided Waves
Copyright (C) 2021-2022  Kang Yang. This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.  
You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.  

-----------------------------------------------------------------------------------------------------------------------------------------
IF THIS CODE IS USED FOR A RESEARCH PUBLICATION, please cite (https://doi.org/10.1038/s41597-025-05300-5):  
Kang Yang, et al. "Dataset on Guided Waves collected from Long-Term Structural Health Monitoring under Uncontrolled and Highly Dynamic Conditions". 
