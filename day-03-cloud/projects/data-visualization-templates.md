# Data Visualization Project Templates
## Ready-to-Use Templates for Classroom Projects

## Template 1: Temperature Log

### Purpose
Track temperature over time and visualize trends

### Setup in Google Sheets

**Column Headers:**
- A1: Date
- B1: Time
- C1: Temperature (°C)
- D1: Location (optional)

**Sample Data:**
```
Date       | Time  | Temperature | Location
2024-01-15 | 08:00 | 22          | Classroom
2024-01-15 | 10:00 | 24          | Classroom
2024-01-15 | 12:00 | 26          | Classroom
2024-01-15 | 14:00 | 28          | Classroom
2024-01-15 | 16:00 | 25          | Classroom
```

### Creating the Chart

1. **Select Data:**
   - Click and drag to select Time and Temperature columns

2. **Insert Chart:**
   - Insert → Chart
   - Chart type: Line chart

3. **Customize:**
   - Title: "Temperature Over Time"
   - X-axis: Time
   - Y-axis: Temperature (°C)
   - Add gridlines
   - Choose colors

### Analysis Questions
- What time was hottest/coldest?
- What is the average temperature?
- What pattern do you see?
- Why might temperature change?

---

## Template 2: Light Level Monitoring

### Purpose
Monitor light levels throughout the day

### Setup

**Column Headers:**
- A1: Time
- B1: Light Level (0-1023)
- C1: Condition (Bright/Normal/Dark)

### Sample Data with Formula

**Column C Formula:**
```
=IF(B2>700, "Bright", IF(B2>300, "Normal", "Dark"))
```

**Sample Data:**
```
Time  | Light Level | Condition
06:00 | 50          | Dark
08:00 | 200         | Dark
10:00 | 600         | Normal
12:00 | 950         | Bright
14:00 | 800         | Bright
16:00 | 400         | Normal
18:00 | 100         | Dark
```

### Chart Options

**Option 1: Line Chart**
- Shows light level over time
- Easy to see trends

**Option 2: Bar Chart**
- Compares different times
- Good for discrete data

**Option 3: Pie Chart**
- Shows proportion of Bright/Normal/Dark
- Good for summary

### Analysis
- When is it brightest?
- How much time in each condition?
- What affects light levels?

---

## Template 3: Plant Growth Tracker

### Purpose
Track plant growth and environmental conditions

### Setup

**Column Headers:**
- A1: Date
- B1: Day Number
- C1: Height (cm)
- D1: Moisture Level
- E1: Light Hours
- F1: Temperature

### Sample Data

```
Date       | Day | Height | Moisture | Light | Temp
2024-01-01 | 1   | 2      | 600      | 8     | 22
2024-01-05 | 5   | 3      | 550      | 8     | 23
2024-01-10 | 10  | 5      | 500      | 9     | 24
2024-01-15 | 15  | 8      | 450      | 10    | 25
2024-01-20 | 20  | 12     | 400      | 10    | 26
```

### Multiple Charts

**Chart 1: Growth Over Time**
- Line chart: Day vs. Height
- Shows growth rate

**Chart 2: Conditions Over Time**
- Multiple lines: Moisture, Light, Temperature
- Shows environmental factors

**Chart 3: Correlation**
- Scatter plot: Moisture vs. Growth
- Shows relationships

### Analysis
- How fast is the plant growing?
- What conditions affect growth?
- Is there a correlation between factors?

---

## Template 4: Classroom Environment Monitor

### Purpose
Monitor classroom conditions for optimal learning

### Setup

**Column Headers:**
- A1: Date/Time
- B1: Temperature (°C)
- C1: Humidity (%)
- D1: Light Level
- E1: Noise Level (optional)
- F1: Comfort Rating

### Sample Data

```
DateTime        | Temp | Humidity | Light | Comfort
2024-01-15 08:00| 22   | 45       | 600   | Good
2024-01-15 10:00| 24   | 50       | 800   | Good
2024-01-15 12:00| 26   | 55       | 900   | Warm
2024-01-15 14:00| 28   | 60       | 850   | Hot
2024-01-15 16:00| 25   | 52       | 400   | Good
```

### Charts

**Chart 1: Temperature and Humidity**
- Dual-axis line chart
- Shows both on same graph

**Chart 2: Comfort Over Time**
- Bar chart by time
- Color-coded by comfort level

### Analysis
- What times are most comfortable?
- What affects comfort?
- How can we improve conditions?

---

## Template 5: Sensor Comparison

### Purpose
Compare readings from multiple sensors

### Setup

**Column Headers:**
- A1: Time
- B1: Sensor 1 (Location 1)
- C1: Sensor 2 (Location 2)
- D1: Sensor 3 (Location 3)
- E1: Average

### Sample Data with Formula

**Column E Formula:**
```
=AVERAGE(B2:D2)
```

**Sample Data:**
```
Time  | Sensor 1 | Sensor 2 | Sensor 3 | Average
08:00 | 22       | 23       | 21       | 22
10:00 | 24       | 25       | 23       | 24
12:00 | 26       | 27       | 25       | 26
```

### Chart

**Multi-line Chart:**
- All sensors on same graph
- Average line highlighted
- Easy to compare

### Analysis
- Which sensor reads highest/lowest?
- Are sensors consistent?
- What causes differences?

---

## Template 6: Daily Summary

### Purpose
Create daily summaries of sensor data

### Setup

**Sheet 1: Raw Data**
- All individual readings

**Sheet 2: Daily Summary**
- A1: Date
- B1: Max Temperature
- C1: Min Temperature
- D1: Average Temperature
- E1: Max Light
- F1: Min Light
- G1: Average Light

### Formulas for Summary

**Max Temperature:**
```
=MAX(Sheet1!C:C)
```

**Min Temperature:**
```
=MIN(Sheet1!C:C)
```

**Average Temperature:**
```
=AVERAGE(Sheet1!C:C)
```

### Chart

**Bar Chart:**
- Compare daily averages
- Shows trends over days
- Easy to see patterns

---

## Template 7: Event Log

### Purpose
Log events and their conditions

### Setup

**Column Headers:**
- A1: Date/Time
- B1: Event Type
- C1: Temperature
- D1: Light Level
- E1: Notes

### Sample Data

```
DateTime        | Event      | Temp | Light | Notes
2024-01-15 10:30| Motion     | 24   | 700   | Person entered
2024-01-15 11:15| Button     | 25   | 750   | Student pressed
2024-01-15 12:00| Alarm      | 26   | 800   | Temperature high
```

### Chart

**Timeline Chart:**
- Events on timeline
- Color-coded by type
- Shows when events occur

---

## General Chart Creation Steps

### Step 1: Prepare Data
- Organize in columns
- Use clear headers
- Ensure data is consistent
- Remove empty rows

### Step 2: Select Data
- Click first cell
- Drag to select range
- Include headers
- Select all relevant columns

### Step 3: Insert Chart
- Go to Insert menu
- Click Chart
- Choose chart type
- Chart appears automatically

### Step 4: Customize
- Add title
- Label axes
- Choose colors
- Add legend
- Format numbers

### Step 5: Analyze
- What does chart show?
- What patterns exist?
- What questions can you answer?
- What actions should be taken?

---

## Chart Type Guide

### Line Chart
**Best for:** Trends over time
**Example:** Temperature throughout day

### Bar Chart
**Best for:** Comparing categories
**Example:** Average temperature by location

### Pie Chart
**Best for:** Showing proportions
**Example:** Percentage of time in each condition

### Scatter Plot
**Best for:** Relationships between variables
**Example:** Temperature vs. Light level

### Area Chart
**Best for:** Cumulative data over time
**Example:** Total sensor readings per day

---

## Analysis Questions Template

### For Any Data Set

**Descriptive Questions:**
- What is the maximum value?
- What is the minimum value?
- What is the average?
- What is the range?

**Pattern Questions:**
- What patterns do you see?
- Are there cycles or trends?
- What times show interesting data?
- Are there outliers?

**Comparison Questions:**
- How do different times compare?
- How do different locations compare?
- How do different days compare?

**Causal Questions:**
- What might cause these patterns?
- What factors affect the data?
- How do variables relate?

**Action Questions:**
- What should we do based on this data?
- How can we improve conditions?
- What changes should we make?

---

## Tips for Success

1. **Start Simple:** Begin with basic charts
2. **Add Complexity:** Add more data gradually
3. **Test Formulas:** Verify calculations
4. **Label Clearly:** Use descriptive titles
5. **Choose Right Type:** Match chart to data
6. **Tell a Story:** Charts should communicate
7. **Ask Questions:** Analysis is key
8. **Iterate:** Improve based on feedback

---

## Classroom Applications

### Mathematics
- Graphing functions
- Statistics and averages
- Data analysis
- Pattern recognition

### Science
- Experiment data
- Observations over time
- Environmental monitoring
- Scientific method

### Technology
- System monitoring
- Performance tracking
- Data logging
- IoT applications

### Social Studies
- Survey data
- Historical trends
- Population data
- Economic indicators

---

Remember: The goal is not just to create charts, but to understand what the data tells us and how we can use that information!

