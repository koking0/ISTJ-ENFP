<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import MsgTypeCntChart from '../components/MsgTypeCntChart.vue';
import MonthMsgCntChart from '../components/MonthMsgCntChart.vue';
import MaxLengthMsgImg from '../components/MaxLengthMsgImg.vue';
import CalendarHeatmapChart from '../components/CalendarHeatmapChart.vue';
import WordCloudChart from '../components/WordCloudChart.vue';

defineProps({
  msg: String,
});

const startTime = new Date('2022-07-03 13:00:35').getTime();
const timeDiff = ref('');

const updateTimeDiff = () => {
  const now = new Date().getTime();
  const diff = now - startTime; // 时间差毫秒数

  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((diff % (1000 * 60)) / 1000);

  timeDiff.value = `${days} 天 ${hours} 时 ${minutes} 分 ${seconds} 秒`;
};

let interval;
onMounted(() => {
  updateTimeDiff(); // 初始化时间差
  interval = setInterval(updateTimeDiff, 1000); // 每秒更新时间差
});

onUnmounted(() => {
  clearInterval(interval); // 清理定时器
});
</script>

<template>
  <h1>{{ msg }}</h1>
  
  <div style="margin-top: 50px;">我们第一次聊天在 <br /> 2022-07-03 13:00:35</div>
  <div style="margin-bottom: 50px;">距今已有 <br /> {{ timeDiff }}</div>

  <MsgTypeCntChart />
  <MonthMsgCntChart />
  <MaxLengthMsgImg />
  <WordCloudChart />
  <CalendarHeatmapChart />
</template>

<style scoped>

</style>
