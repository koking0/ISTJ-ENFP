<script setup>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent
} from "echarts/components";
import VChart from "vue-echarts";
import { ref } from "vue";

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent
]);

const msg_type_cnt_option = ref({
  title: {
    text: "消息类型统计",
    left: "left"
  },
  tooltip: {
    trigger: "item",
    formatter: "{a} <br/>{b} : {c} ({d}%)"
  },
  series: [
    {
      name: 'ISTJ',
      type: 'pie',
      radius: ['40%', '70%'],
      center: ['25%', '50%'],
      itemStyle: {
        borderRadius: 5
      },
      data: [
        { "value": 53601, "name": "文字消息" },
        { "value": 4205, "name": "emoji" },
        { "value": 1699, "name": "其他" },
        { "value": 1514, "name": "图片" },
        { "value": 674, "name": "语音消息" },
        { "value": 408, "name": "其他" },
        { "value": 113, "name": "语音消息" },
        { "value": 108, "name": "微信电话" },
        { "value": 32, "name": "撤回消息或拒收" },
        { "value": 4, "name": "图片" },
        { "value": 3, "name": "位置" }
      ]
    },
    {
      name: 'ENFP',
      type: 'pie',
      radius: ['40%', '70%'],
      center: ['75%', '50%'],
      itemStyle: {
        borderRadius: 5
      },
      data: [
        { "value": 61591, "name": "文字消息" },
        { "value": 6547, "name": "emoji" },
        { "value": 2732, "name": "图片" },
        { "value": 1811, "name": "其他" },
        { "value": 458, "name": "撤回消息或拒收" },
        { "value": 221, "name": "其他" },
        { "value": 76, "name": "语音消息" },
        { "value": 76, "name": "语音消息" },
        { "value": 28, "name": "微信电话" },
        { "value": 10, "name": "位置" },
        { "value": 8, "name": "图片" }
      ]
    }
  ]
});
</script>

<template>
  <v-chart :option="msg_type_cnt_option" style="height: 500px; width: 1000px;"/>
  <div style="width: 1000px;">
    这是我们互相发的消息类型统计，可以看到，我们都是文字消息为主，emoji次之，图片和语音消息也有一些，其他类型的消息很少。
  </div>
  <div style="width: 1000px; margin-bottom: 100px;">
    据统计，我一共给你发了62361条消息，而你给我发了73558条消息。
  </div>
</template>

<style scoped>

</style>
