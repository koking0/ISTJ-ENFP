<script setup>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { BarChart, LineChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  GridComponent,
  LegendComponent
} from "echarts/components";
import VChart from "vue-echarts";
import { ref } from "vue";

use([
  CanvasRenderer,
  BarChart, LineChart,
  TitleComponent,
  TooltipComponent,
  GridComponent,
  LegendComponent
]);

const month_msg_cnt_option = ref({
  title: {
    text: "每月消息统计",
    left: "left"
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'cross',
      crossStyle: {
        color: '#999'
      }
    }
  },
  legend: {
    data: ['ISTJ', 'ENFP']
  },
  xAxis: [
    {
      type: 'category',
      data: ['2022-07', '2022-08', '2022-09', '2022-10', '2022-11', '2022-12', '2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06', '2023-07', '2023-08', '2023-09', '2023-10', '2023-11', '2023-12', '2024-01', '2024-02', "平均"],
      axisPointer: {
        type: 'shadow'
      }
    }
  ],
  yAxis: [
    {
      type: 'value',
      name: '消息数量',
      min: 0,
      max: 10000,
      interval: 1000,
      axisLabel: {
        formatter: '{value} 条'
      }
    },
    {
      type: 'value',
      name: '平均消息长度',
      min: 0,
      max: 50,
      interval: 10,
      axisLabel: {
        formatter: '{value} 字'
      }
    }
  ],
  series: [
    {
      name: 'ISTJ',
      type: 'bar',
      tooltip: {
        valueFormatter: function (value) {
          return value + ' 条';
        }
      },
      data: [8, 51, 78, 189, 83, 42, 445, 285, 2024, 3823, 6969, 6300, 7982, 2515, 6366, 7214, 4762, 5605, 6881, 739, 3118]
    },
    {
      name: 'ENFP',
      type: 'bar',
      tooltip: {
        valueFormatter: function (value) {
          return value + ' 条';
        }
      },
      data: [12, 48, 141, 363, 144, 52, 678, 589, 2766, 5299, 8919, 6765, 10405, 3215, 7124, 7457, 5076, 6187, 7314, 1004, 3677]
    },
    {
      name: 'ISTJ',
      type: 'line',
      yAxisIndex: 1,
      tooltip: {
        valueFormatter: function (value) {
          return value + ' 字';
        }
      },
      data: [8.38, 8.73, 45.73, 14.54, 17.05, 8.0, 12.23, 11.88, 10.99, 11.03, 10.32, 9.65, 11.07, 13.83, 10.16, 10.58, 11.23, 10.8, 9.37, 8.36, 12.7],
    },
    {
      name: 'ENFP',
      type: 'line',
      yAxisIndex: 1,
      tooltip: {
        valueFormatter: function (value) {
          return value + ' 字';
        }
      },
      data: [6.22, 8.74, 8.93, 9.56, 7.74, 10.83, 6.93, 8.04, 8.65, 6.57, 7.19, 6.76, 7.56, 7.79, 6.87, 6.97, 7.02, 7.31, 7.34, 6.97, 7.69]
    }
  ]
});
</script>

<template>
  <v-chart :option="month_msg_cnt_option" style="height: 500px; width: 1000px;" />

  <div style="width: 1000px;">
    这是我们每个月的消息数量（柱状图）和平均消息长度（折线图），可以发现，虽然你每个月的消息数量比我多，但是我的平均消息长度要比你长。
  </div>
  <div style="width: 1000px;">
    2022年9月22日，因为南开的项目，我给你发了一条长达1379个字的消息，而由于该月消息数量太少，因此极大的拉高了我这个月的平均消息长度，产生了一个峰值。
  </div>
  <div style="width: 1000px;">
    2023年8月，我们去了上海和苏州旅游，因此消息变少了。
  </div>
  <div style="width: 1000px;">
    最后平均下来，我每个月给你发了3118条消息，平均长度为12.7字，大约40万字，而你每个月给我发了3677条消息，平均长度为7.69字，大约28万字。
  </div>
  <div style="width: 1000px; margin-bottom: 100px;">
    你赢在了数量，而我胜在了质量，嘿嘿，扳回一局~
  </div>
</template>

<style scoped></style>
