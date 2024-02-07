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

// prettier-ignore
let timeData = ['2023-10-24', '2023-10-25', '2023-10-26', '2023-10-27', '2023-10-28', '2023-10-29', '2023-10-30', '2023-10-31', '2023-11-01', '2023-11-02', '2023-11-03', '2023-11-04', '2023-11-05', '2023-11-06', '2023-11-07', '2023-11-08', '2023-11-09', '2023-11-10', '2023-11-11', '2023-11-12', '2023-11-13', '2023-11-14', '2023-11-15', '2023-11-16', '2023-11-17', '2023-11-18', '2023-11-19', '2023-11-20', '2023-11-21', '2023-11-22', '2023-11-23', '2023-11-24', '2023-11-25', '2023-11-26', '2023-11-27', '2023-11-28', '2023-11-29', '2023-11-30', '2023-12-01', '2023-12-02', '2023-12-03', '2023-12-04', '2023-12-05', '2023-12-06', '2023-12-07', '2023-12-08', '2023-12-09', '2023-12-10', '2023-12-11', '2023-12-12', '2023-12-13', '2023-12-14', '2023-12-16', '2023-12-17', '2023-12-18', '2023-12-19', '2023-12-20', '2023-12-21', '2023-12-22', '2023-12-23', '2023-12-24', '2023-12-25', '2023-12-26', '2023-12-27', '2023-12-28', '2023-12-29', '2023-12-30', '2023-12-31', '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24', '2024-01-25', '2024-01-26', '2024-01-27', '2024-01-28', '2024-01-29', '2024-01-30', '2024-01-31', '2024-02-01', '2024-02-02', '2024-02-03']
;

timeData = timeData.map(function (str) {
  return str;
});

const day_msg_sentiment_option = ref({
  title: {
    text: '每日情感分析',
    left: 'left'
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      animation: false
    }
  },
  legend: {
    data: ['正向', '负向'],
    left: 400
  },
  toolbox: {
    feature: {
      dataZoom: {
        yAxisIndex: 'none'
      },
      restore: {},
      saveAsImage: {}
    }
  },
  axisPointer: {
    link: [
      {
        xAxisIndex: 'all'
      }
    ]
  },
  dataZoom: [
    {
      show: true,
      realtime: true,
      start: 30,
      end: 70,
      xAxisIndex: [0, 1]
    },
    {
      type: 'inside',
      realtime: true,
      start: 30,
      end: 70,
      xAxisIndex: [0, 1]
    }
  ],
  grid: [
    {
      left: 60,
      right: 50,
      height: '35%'
    },
    {
      left: 60,
      right: 50,
      top: '55%',
      height: '35%'
    }
  ],
  xAxis: [
    {
      type: 'category',
      boundaryGap: false,
      axisLine: { onZero: true },
      data: timeData
    },
    {
      gridIndex: 1,
      type: 'category',
      boundaryGap: false,
      axisLine: { onZero: true },
      data: timeData,
      position: 'top'
    }
  ],
  yAxis: [
    {
      name: '正向(条)',
      type: 'value',
      max: 500
    },
    {
      gridIndex: 1,
      name: '负向(条)',
      type: 'value',
      inverse: true
    }
  ],
  series: [
    {
      name: '正向',
      type: 'line',
      symbolSize: 8,

      // prettier-ignore
      data: [157, 275, 253, 226, 234, 178, 281, 121, 178, 170, 53, 75, 97, 127, 182, 188, 165, 162, 118, 51, 151, 101, 156, 84, 123, 52, 97, 160, 213, 175, 61, 69, 59, 83, 125, 76, 101, 132, 122, 161, 101, 117, 145, 189, 277, 56, 154, 125, 311, 208, 299, 16, 22, 3, 67, 111, 104, 113, 34, 142, 64, 142, 243, 140, 139, 211, 76, 325, 173, 196, 170, 90, 465, 216, 178, 193, 121, 121, 131, 172, 91, 79, 105, 236, 246, 107, 141, 215, 178, 148, 246, 182, 203, 283, 192, 69, 147, 330, 139, 101]
    },
    {
      name: '负向',
      type: 'line',
      xAxisIndex: 1,
      yAxisIndex: 1,
      symbolSize: 8,

      // prettier-ignore
      data: [199, 280, 328, 336, 301, 206, 461, 155, 254, 216, 85, 78, 90, 150, 292, 289, 169, 268, 133, 33, 191, 122, 341, 92, 141, 94, 134, 162, 418, 168, 37, 83, 49, 96, 161, 88, 145, 230, 126, 227, 142, 177, 197, 330, 380, 51, 196, 228, 527, 260, 464, 9, 20, 4, 68, 160, 212, 105, 45, 123, 77, 204, 341, 144, 157, 288, 93, 406, 178, 218, 250, 108, 651, 343, 314, 169, 120, 157, 175, 329, 92, 97, 101, 288, 347, 128, 140, 330, 249, 197, 413, 250, 290, 444, 333, 72, 221, 607, 257, 107]
    }
  ]
});
</script>

<template>
  <v-chart :option="day_msg_sentiment_option" style="height: 500px; width: 1000px;" />
  <div style="width: 1000px;">
    通过模型来判断我们每天的聊天内容是正向还是负向的，可以很好的反应我们的情感变化。
  </div>
  <div style="width: 1000px; margin-bottom: 100px;">
    不过它呈现出了一种类似镜像的关系，有可能是因为即使我们吵架，也会在当天和好，所以相互抵消了。
  </div>
</template>

<style scoped>

</style>
