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

const hour_msg_cnt_option = ref({
  title: {
    text: "每日分小时消息统计",
    left: "left"
  },
  angleAxis: {
    type: 'category',
    data: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
  },
  radiusAxis: {},
  polar: {},
  series: [
    {
      type: 'bar',
      data: [3243.0, 762.0, 110.0, 0, 1.0, 48.0, 68.0, 274.0, 1407.0, 2839.0, 3041.0, 3866.0, 3854.0, 3618.0, 3962.0, 3628.0, 4060.0, 4053.0, 3348.0, 3303.0, 2833.0, 2935.0, 4296.0, 6812.0],
      coordinateSystem: 'polar',
      name: 'ISTJ',
      stack: 'a',
      emphasis: {
        focus: 'series'
      }
    },
    {
      type: 'bar',
      data: [3524.0, 906.0, 190.0, 3.0, 0, 45.0, 139.0, 254.0, 1535.0, 3264.0, 3260.0, 4258.0, 4616.0, 4495.0, 4537.0, 4520.0, 4932.0, 4697.0, 4069.0, 4200.0, 3496.0, 3774.0, 5149.0, 7695.0],
      coordinateSystem: 'polar',
      name: 'ENFP',
      stack: 'a',
      emphasis: {
        focus: 'series'
      }
    }
  ],
  legend: {
    show: true,
    data: ['ISTJ', 'ENFP']
  }
});
</script>

<template>
  <v-chart :option="hour_msg_cnt_option" style="height: 500px; width: 1000px;" />
  <div style="width: 1000px; margin-bottom: 100px;">
    可以发现，我们的聊天时间主要集中在晚上，尤其是在晚上11点，达到了一个高峰。稍微有一丢丢的晚了捏，要早睡早起哦~
  </div>
</template>

<style scoped>

</style>
