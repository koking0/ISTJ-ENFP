<script setup>
import 'echarts-wordcloud';
import { inject, onMounted } from "vue"
import 'echarts-wordcloud'

let $echarts = inject("echarts")
onMounted(() => {
  let mychart1 = $echarts.init(document.getElementById("istj_container"))
  let mychart2 = $echarts.init(document.getElementById("enfp_container"))
  let option1 = {
    series: [{
      type: 'wordCloud',
      shape: 'circle',
      left: 'center',
      top: 'center',
      width: '90%',
      height: '90%',
      right: null,
      bottom: null,
      sizeRange: [12, 60],
      rotationRange: [-90, 90],
      rotationStep: 45,
      gridSize: 30,
      drawOutOfBound: false,
      layoutAnimation: true,
      textStyle: {
        fontFamily: 'sans-serif',
        fontWeight: 'bold',
        color: function () {
          return 'rgb(' + [
            Math.round(Math.random() * 160),
            Math.round(Math.random() * 160),
            Math.round(Math.random() * 160)
          ].join(',') + ')';
        }
      },
      emphasis: {
        focus: 'self',
        textStyle: {
          textShadowBlur: 10,
          textShadowColor: '#333'
        }
      },
      data: [{'name': '宝贝', 'value': 2359}, {'name': '宝宝', 'value': 2001}, {'name': '旺柴', 'value': 1127}, {'name': '一个', 'value': 1098}, {'name': '没事', 'value': 804}, {'name': '感觉', 'value': 784}, {'name': '破涕为笑', 'value': 654}, {'name': '喜欢', 'value': 606}, {'name': '可怜', 'value': 502}, {'name': '苦涩', 'value': 454}, {'name': '回来', 'value': 452}, {'name': '哦哦哦', 'value': 448}, {'name': '流泪', 'value': 448}, {'name': '啊啊啊', 'value': 418}, {'name': '好滴', 'value': 416}, {'name': '好像', 'value': 412}, {'name': '东西', 'value': 375}, {'name': '皱眉', 'value': 372}, {'name': '老师', 'value': 367}, {'name': '一点', 'value': 358}, {'name': '捂脸', 'value': 352}, {'name': '事情', 'value': 343}, {'name': '好好', 'value': 342}, {'name': '确实', 'value': 340}, {'name': '亲亲', 'value': 332}, {'name': '真的', 'value': 324}, {'name': 'emmm', 'value': 316}, {'name': '明天', 'value': 315}, {'name': '时间', 'value': 304}, {'name': '晚上', 'value': 297}, {'name': '肯定', 'value': 280}, {'name': '不想', 'value': 278}, {'name': '记得', 'value': 271}, {'name': '回去', 'value': 255}, {'name': '不好', 'value': 251}, {'name': '吃饭', 'value': 246}, {'name': '休息', 'value': 244}, {'name': '不行', 'value': 239}, {'name': '晚安', 'value': 224}, {'name': '那种', 'value': 222}, {'name': '项目', 'value': 221}, {'name': '刚才', 'value': 217}, {'name': '工作室', 'value': 216}, {'name': 'OK', 'value': 211}, {'name': '代码', 'value': 207}, {'name': '学校', 'value': 206}, {'name': '哈哈哈', 'value': 203}, {'name': '学习', 'value': 199}, {'name': '估计', 'value': 194}, {'name': '不用', 'value': 184}, {'name': '两个', 'value': 179}, {'name': '别人', 'value': 178}, {'name': '下午', 'value': 171}, {'name': '手机', 'value': 170}, {'name': '对不起', 'value': 166}, {'name': '理解', 'value': 160}, {'name': '还好', 'value': 157}, {'name': '宿舍', 'value': 154}, {'name': '想法', 'value': 153}, {'name': '几个', 'value': 152}, {'name': '北京', 'value': 151}, {'name': '呜呜', 'value': 151}, {'name': '厉害', 'value': 149}, {'name': '很多', 'value': 147}, {'name': '抱抱', 'value': 146}, {'name': '差不多', 'value': 145}, {'name': '女生', 'value': 145}, {'name': '会议', 'value': 143}, {'name': '有没有', 'value': 139}, {'name': '一会', 'value': 139}, {'name': '问问', 'value': 138}, {'name': '超级', 'value': 138}, {'name': '老婆', 'value': 138}, {'name': 'Emm', 'value': 136}, {'name': '机智', 'value': 136}, {'name': '电脑', 'value': 134}, {'name': '哈哈哈哈', 'value': 133}, {'name': '地方', 'value': 133}, {'name': '工作', 'value': 132}, {'name': '到时候', 'value': 131}, {'name': '还要', 'value': 131}, {'name': '我错', 'value': 131}, {'name': '大概', 'value': 130}, {'name': '实习', 'value': 129}, {'name': '同学', 'value': 129}, {'name': '特别', 'value': 128}, {'name': '上课', 'value': 126}, {'name': '我刚', 'value': 126}, {'name': '不至于', 'value': 125}, {'name': '是因为', 'value': 125}, {'name': '不了', 'value': 124}, {'name': '好不好', 'value': 124}, {'name': '发呆', 'value': 123}, {'name': '生气', 'value': 122}, {'name': '想想', 'value': 121}, {'name': '申请', 'value': 121}, {'name': '前端', 'value': 120}, {'name': '中午', 'value': 119}, {'name': '可爱', 'value': 117}, {'name': '男生', 'value': 116}],
    }]
  }
  let option2 = {
    series: [{
      type: 'wordCloud',
      shape: 'circle',
      left: 'center',
      top: 'center',
      width: '70%',
      height: '80%',
      right: null,
      bottom: null,
      sizeRange: [12, 60],
      rotationRange: [-90, 90],
      rotationStep: 45,
      gridSize: 30,
      drawOutOfBound: false,
      layoutAnimation: true,
      textStyle: {
        fontFamily: 'sans-serif',
        fontWeight: 'bold',
        color: function () {
          return 'rgb(' + [
            Math.round(Math.random() * 160),
            Math.round(Math.random() * 160),
            Math.round(Math.random() * 160)
          ].join(',') + ')';
        }
      },
      emphasis: {
        focus: 'self',
        textStyle: {
          textShadowBlur: 10,
          textShadowColor: '#333'
        }
      },
      data: [{'name': '宝宝', 'value': 1925}, {'name': '破涕为笑', 'value': 1665}, {'name': '一个', 'value': 1060}, {'name': '感觉', 'value': 1049}, {'name': '喜欢', 'value': 943}, {'name': '真的', 'value': 703}, {'name': '宝贝', 'value': 547}, {'name': '不想', 'value': 545}, {'name': '刚才', 'value': 447}, {'name': '那种', 'value': 408}, {'name': '可怜', 'value': 351}, {'name': '事情', 'value': 340}, {'name': '亲亲', 'value': 335}, {'name': '捂脸', 'value': 314}, {'name': '女生', 'value': 312}, {'name': '朋友', 'value': 301}, {'name': '没事', 'value': 295}, {'name': '苦涩', 'value': 285}, {'name': '一点', 'value': 284}, {'name': '男生', 'value': 261}, {'name': '不好', 'value': 249}, {'name': '我俩', 'value': 248}, {'name': '撇嘴', 'value': 246}, {'name': '明天', 'value': 243}, {'name': '很多', 'value': 242}, {'name': '睡觉', 'value': 237}, {'name': '不用', 'value': 230}, {'name': '啊啊啊', 'value': 222}, {'name': '晚上', 'value': 214}, {'name': '对方', 'value': 214}, {'name': '别人', 'value': 212}, {'name': '流泪', 'value': 205}, {'name': '难过', 'value': 200}, {'name': '两个', 'value': 199}, {'name': '好像', 'value': 198}, {'name': '一会儿', 'value': 197}, {'name': '希望', 'value': 191}, {'name': '告诉', 'value': 188}, {'name': '吃饭', 'value': 185}, {'name': '是因为', 'value': 183}, {'name': '东西', 'value': 180}, {'name': '前端', 'value': 177}, {'name': '心情', 'value': 175}, {'name': '委屈', 'value': 169}, {'name': '开心', 'value': 168}, {'name': '晚安', 'value': 167}, {'name': '代码', 'value': 166}, {'name': '宿舍', 'value': 166}, {'name': '反正', 'value': 165}, {'name': '打算', 'value': 164}, {'name': '裂开', 'value': 164}, {'name': '我要', 'value': 163}, {'name': '时间', 'value': 161}, {'name': '工作室', 'value': 157}, {'name': '害羞', 'value': 156}, {'name': '呜呜', 'value': 155}, {'name': '生气', 'value': 155}, {'name': '哈哈哈', 'value': 143}, {'name': '发现', 'value': 142}, {'name': '老公', 'value': 142}, {'name': '转圈', 'value': 140}, {'name': '实习', 'value': 138}, {'name': '昨天', 'value': 137}, {'name': '项目', 'value': 136}, {'name': '不了', 'value': 134}, {'name': '老师', 'value': 134}, {'name': '几个', 'value': 132}, {'name': '对象', 'value': 132}, {'name': '电脑', 'value': 130}, {'name': '为啥', 'value': 127}, {'name': '微笑', 'value': 126}, {'name': '说话', 'value': 124}, {'name': '我会', 'value': 123}, {'name': '想着', 'value': 123}, {'name': '衣服', 'value': 123}, {'name': '嗷嗷', 'value': 123}, {'name': '确实', 'value': 121}, {'name': '尴尬', 'value': 121}, {'name': '记得', 'value': 119}, {'name': '好滴', 'value': 118}, {'name': '回去', 'value': 117}, {'name': '峰哥', 'value': 116}, {'name': '脸红', 'value': 116}, {'name': '好看', 'value': 115}, {'name': '回来', 'value': 114}, {'name': '嘿嘿', 'value': 114}, {'name': '不到', 'value': 111}, {'name': '学校', 'value': 111}, {'name': '谈恋爱', 'value': 111}, {'name': '想要', 'value': 110}, {'name': '朱曼', 'value': 110}, {'name': '舍友', 'value': 109}, {'name': '估计', 'value': 108}, {'name': '毕竟', 'value': 108}, {'name': '只能', 'value': 108}, {'name': '没法', 'value': 108}, {'name': '关系', 'value': 108}, {'name': 'ztx', 'value': 107}, {'name': '想法', 'value': 107}, {'name': '这件', 'value': 107}],
    }]
  }
  mychart1.setOption(option1)
  mychart2.setOption(option2)
})
</script>

<template>
  <h1>ISTJ 的词云图</h1>
  <div style="width: 1000px; height: 500px;" id="istj_container"></div>
  <h1>ENFP 的词云图</h1>
  <div style="width: 1000px; height: 500px; margin-bottom: 100px;" id="enfp_container"> </div>
</template>

<style scoped>
#istj_container {
  width: 100%;
  height: 100%;
}

#enfp_container {
  width: 100%;
  height: 100%;
}
</style>
