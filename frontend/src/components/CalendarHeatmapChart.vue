<script setup>
import * as echarts from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { HeatmapChart } from "echarts/charts";
import {
  TitleComponent,
  VisualMapComponent,
  TooltipComponent,
  CalendarComponent,
  LegendComponent
} from "echarts/components";
import VChart from "vue-echarts";
import { ref } from "vue";

function getDateMsgCntData(year) {
  const dateCntList = [['2022-07-03', 20], ['2022-08-16', 63], ['2022-08-31', 36], ['2022-09-01', 5], ['2022-09-02', 68], ['2022-09-04', 5], ['2022-09-06', 13], ['2022-09-08', 16], ['2022-09-09', 3], ['2022-09-12', 20], ['2022-09-13', 17], ['2022-09-14', 2], ['2022-09-15', 7], ['2022-09-20', 3], ['2022-09-22', 57], ['2022-09-28', 3], ['2022-10-06', 7], ['2022-10-08', 3], ['2022-10-14', 6], ['2022-10-15', 14], ['2022-10-17', 56], ['2022-10-18', 1], ['2022-10-19', 45], ['2022-10-21', 7], ['2022-10-24', 74], ['2022-10-26', 143], ['2022-10-27', 185], ['2022-11-01', 1], ['2022-11-03', 36], ['2022-11-06', 20], ['2022-11-08', 67], ['2022-11-09', 25], ['2022-11-14', 34], ['2022-11-29', 12], ['2022-11-30', 32], ['2022-12-01', 30], ['2022-12-10', 4], ['2022-12-20', 56], ['2022-12-31', 4], ['2023-01-05', 198], ['2023-01-09', 156], ['2023-01-10', 76], ['2023-01-11', 178], ['2023-01-13', 12], ['2023-01-14', 36], ['2023-01-15', 120], ['2023-01-23', 126], ['2023-01-25', 7], ['2023-01-29', 17], ['2023-01-30', 178], ['2023-02-03', 26], ['2023-02-06', 4], ['2023-02-07', 6], ['2023-02-08', 4], ['2023-02-14', 4], ['2023-02-15', 3], ['2023-02-18', 77], ['2023-02-19', 35], ['2023-02-20', 23], ['2023-02-21', 127], ['2023-02-22', 48], ['2023-02-25', 228], ['2023-02-26', 37], ['2023-02-27', 157], ['2023-02-28', 83], ['2023-03-01', 177], ['2023-03-02', 12], ['2023-03-03', 4], ['2023-03-04', 119], ['2023-03-05', 15], ['2023-03-07', 14], ['2023-03-08', 17], ['2023-03-09', 59], ['2023-03-10', 40], ['2023-03-11', 72], ['2023-03-12', 37], ['2023-03-13', 43], ['2023-03-14', 192], ['2023-03-16', 151], ['2023-03-17', 53], ['2023-03-18', 118], ['2023-03-19', 555], ['2023-03-20', 100], ['2023-03-21', 105], ['2023-03-22', 121], ['2023-03-23', 258], ['2023-03-24', 365], ['2023-03-25', 48], ['2023-03-26', 79], ['2023-03-27', 560], ['2023-03-28', 252], ['2023-03-29', 398], ['2023-03-30', 410], ['2023-03-31', 293], ['2023-04-01', 89], ['2023-04-02', 269], ['2023-04-03', 197], ['2023-04-04', 147], ['2023-04-05', 245], ['2023-04-06', 119], ['2023-04-07', 388], ['2023-04-08', 115], ['2023-04-09', 176], ['2023-04-10', 427], ['2023-04-11', 379], ['2023-04-12', 275], ['2023-04-13', 529], ['2023-04-14', 531], ['2023-04-15', 174], ['2023-04-16', 329], ['2023-04-17', 728], ['2023-04-18', 758], ['2023-04-19', 121], ['2023-04-20', 175], ['2023-04-21', 683], ['2023-04-22', 115], ['2023-04-23', 343], ['2023-04-25', 32], ['2023-04-27', 484], ['2023-04-28', 813], ['2023-04-29', 189], ['2023-04-30', 130], ['2023-05-01', 58], ['2023-05-02', 58], ['2023-05-03', 220], ['2023-05-04', 674], ['2023-05-05', 567], ['2023-05-06', 1457], ['2023-05-07', 314], ['2023-05-08', 1295], ['2023-05-09', 548], ['2023-05-10', 963], ['2023-05-11', 385], ['2023-05-12', 799], ['2023-05-13', 839], ['2023-05-14', 228], ['2023-05-15', 986], ['2023-05-16', 480], ['2023-05-17', 1409], ['2023-05-18', 766], ['2023-05-19', 462], ['2023-05-20', 399], ['2023-05-21', 190], ['2023-05-22', 14], ['2023-05-23', 526], ['2023-05-24', 359], ['2023-05-25', 108], ['2023-05-26', 437], ['2023-05-27', 3], ['2023-05-28', 2], ['2023-05-29', 603], ['2023-05-30', 211], ['2023-05-31', 37], ['2023-06-01', 476], ['2023-06-02', 327], ['2023-06-03', 4], ['2023-06-04', 7], ['2023-06-05', 375], ['2023-06-06', 146], ['2023-06-07', 821], ['2023-06-08', 358], ['2023-06-09', 407], ['2023-06-10', 0], ['2023-06-11', 153], ['2023-06-12', 609], ['2023-06-13', 535], ['2023-06-14', 417], ['2023-06-15', 403], ['2023-06-16', 58], ['2023-06-17', 3], ['2023-06-18', 488], ['2023-06-19', 1205], ['2023-06-20', 605], ['2023-06-21', 837], ['2023-06-22', 461], ['2023-06-23', 477], ['2023-06-24', 282], ['2023-06-25', 53], ['2023-06-26', 507], ['2023-06-27', 817], ['2023-06-28', 641], ['2023-06-29', 598], ['2023-06-30', 461], ['2023-07-01', 949], ['2023-07-02', 728], ['2023-07-03', 820], ['2023-07-04', 703], ['2023-07-05', 710], ['2023-07-06', 603], ['2023-07-07', 492], ['2023-07-08', 485], ['2023-07-09', 450], ['2023-07-10', 355], ['2023-07-11', 365], ['2023-07-12', 307], ['2023-07-13', 434], ['2023-07-14', 582], ['2023-07-15', 645], ['2023-07-16', 456], ['2023-07-17', 1061], ['2023-07-18', 530], ['2023-07-19', 612], ['2023-07-20', 603], ['2023-07-21', 632], ['2023-07-22', 501], ['2023-07-23', 264], ['2023-07-24', 464], ['2023-07-25', 606], ['2023-07-26', 392], ['2023-07-27', 843], ['2023-07-28', 809], ['2023-07-29', 84], ['2023-07-30', 582], ['2023-07-31', 514], ['2023-08-01', 525], ['2023-08-02', 331], ['2023-08-03', 695], ['2023-08-04', 364], ['2023-08-05', 106], ['2023-08-06', 182], ['2023-08-07', 381], ['2023-08-08', 110], ['2023-08-09', 342], ['2023-08-10', 192], ['2023-08-11', 23], ['2023-08-13', 42], ['2023-08-14', 26], ['2023-08-16', 21], ['2023-08-17', 9], ['2023-08-18', 1], ['2023-08-19', 10], ['2023-08-20', 39], ['2023-08-21', 12], ['2023-08-22', 102], ['2023-08-23', 24], ['2023-08-24', 156], ['2023-08-25', 172], ['2023-08-26', 182], ['2023-08-27', 96], ['2023-08-28', 364], ['2023-08-29', 437], ['2023-08-30', 170], ['2023-08-31', 404], ['2023-09-01', 508], ['2023-09-02', 331], ['2023-09-03', 272], ['2023-09-04', 323], ['2023-09-05', 402], ['2023-09-06', 321], ['2023-09-07', 441], ['2023-09-08', 280], ['2023-09-09', 393], ['2023-09-10', 550], ['2023-09-11', 330], ['2023-09-12', 695], ['2023-09-13', 599], ['2023-09-14', 301], ['2023-09-15', 1029], ['2023-09-16', 680], ['2023-09-17', 435], ['2023-09-18', 343], ['2023-09-19', 616], ['2023-09-20', 489], ['2023-09-21', 213], ['2023-09-22', 212], ['2023-09-23', 272], ['2023-09-24', 182], ['2023-09-25', 308], ['2023-09-26', 412], ['2023-09-27', 1214], ['2023-09-28', 122], ['2023-09-29', 355], ['2023-09-30', 502], ['2023-10-01', 94], ['2023-10-02', 346], ['2023-10-03', 329], ['2023-10-04', 349], ['2023-10-05', 144], ['2023-10-06', 236], ['2023-10-07', 497], ['2023-10-08', 544], ['2023-10-09', 323], ['2023-10-10', 413], ['2023-10-11', 351], ['2023-10-12', 456], ['2023-10-13', 341], ['2023-10-14', 475], ['2023-10-15', 466], ['2023-10-16', 929], ['2023-10-17', 496], ['2023-10-18', 430], ['2023-10-19', 328], ['2023-10-20', 435], ['2023-10-21', 262], ['2023-10-22', 1196], ['2023-10-23', 220], ['2023-10-24', 419], ['2023-10-25', 666], ['2023-10-26', 664], ['2023-10-27', 604], ['2023-10-28', 583], ['2023-10-29', 411], ['2023-10-30', 1004], ['2023-10-31', 356], ['2023-11-01', 545], ['2023-11-02', 437], ['2023-11-03', 159], ['2023-11-04', 176], ['2023-11-05', 219], ['2023-11-06', 320], ['2023-11-07', 546], ['2023-11-08', 560], ['2023-11-09', 386], ['2023-11-10', 482], ['2023-11-11', 292], ['2023-11-12', 99], ['2023-11-13', 384], ['2023-11-14', 258], ['2023-11-15', 529], ['2023-11-16', 188], ['2023-11-17', 308], ['2023-11-18', 158], ['2023-11-19', 249], ['2023-11-20', 354], ['2023-11-21', 675], ['2023-11-22', 381], ['2023-11-23', 107], ['2023-11-24', 169], ['2023-11-25', 119], ['2023-11-26', 290], ['2023-11-27', 312], ['2023-11-28', 192], ['2023-11-29', 284], ['2023-11-30', 386], ['2023-12-01', 279], ['2023-12-02', 436], ['2023-12-03', 266], ['2023-12-04', 316], ['2023-12-05', 382], ['2023-12-06', 567], ['2023-12-07', 716], ['2023-12-08', 312], ['2023-12-09', 393], ['2023-12-10', 383], ['2023-12-11', 925], ['2023-12-12', 549], ['2023-12-13', 829], ['2023-12-14', 35], ['2023-12-15', 0], ['2023-12-16', 46], ['2023-12-17', 8], ['2023-12-18', 147], ['2023-12-19', 290], ['2023-12-20', 354], ['2023-12-21', 245], ['2023-12-22', 82], ['2023-12-23', 301], ['2023-12-24', 175], ['2023-12-25', 392], ['2023-12-26', 668], ['2023-12-27', 316], ['2023-12-28', 351], ['2023-12-29', 550], ['2023-12-30', 283], ['2023-12-31', 807], ['2024-01-01', 404], ['2024-01-02', 455], ['2024-01-03', 475], ['2024-01-04', 249], ['2024-01-05', 1245], ['2024-01-06', 618], ['2024-01-07', 559], ['2024-01-08', 420], ['2024-01-09', 281], ['2024-01-10', 308], ['2024-01-11', 382], ['2024-01-12', 571], ['2024-01-13', 204], ['2024-01-14', 212], ['2024-01-15', 226], ['2024-01-16', 574], ['2024-01-17', 633], ['2024-01-18', 269], ['2024-01-19', 1], ['2024-01-20', 2], ['2024-01-21', 369], ['2024-01-22', 638], ['2024-01-23', 504], ['2024-01-24', 390], ['2024-01-25', 749], ['2024-01-26', 507], ['2024-01-27', 561], ['2024-01-28', 779], ['2024-01-29', 592], ['2024-01-30', 175], ['2024-01-31', 416], ['2024-02-01', 1039], ['2024-02-02', 441], ['2024-02-03', 229]];
  const data = [];
  for (let i = 0; i < dateCntList.length; i++) {
    if (dateCntList[i][0].startsWith(year)) {
      data.push([echarts.time.format(dateCntList[i][0], '{yyyy}-{MM}-{dd}', false), dateCntList[i][1]]);
    }
  }
  return data;
}

echarts.use([
  CanvasRenderer,
  HeatmapChart,
  TitleComponent,
  TooltipComponent,
  VisualMapComponent,
  CalendarComponent,
  LegendComponent
]);

const calendar_heatmap_option = ref({
  title: {
    text: "日消息热度图",
    left: "left"
  },
  tooltip: {
    position: 'top',
    formatter: function (p) {
      const format = echarts.time.format(p.data[0], '{yyyy}-{MM}-{dd}', false);
      return format + ': ' + p.data[1];
    }
  },
  visualMap: {
    min: 0,
    max: 1500,
    type: 'piecewise',
    orient: 'horizontal',
    left: 'center',
    top: 65
  },
  calendar: [
    {
      top: 120,
      range: '2022',
      cellSize: ['auto', 13],
      itemStyle: {
        borderWidth: 0.5
      }
    },
    {
      top: 250,
      range: '2023',
      cellSize: ['auto', 13],
      itemStyle: {
        borderWidth: 0.5
      }
    },
    {
      top: 380,
      range: '2024',
      cellSize: ['auto', 13],
      itemStyle: {
        borderWidth: 0.5
      }
    }
  ],
  series: [{
    type: 'heatmap',
    coordinateSystem: 'calendar',
    calendarIndex: 0,
    data: getDateMsgCntData("2022")
  },
  {
    type: 'heatmap',
    coordinateSystem: 'calendar',
    calendarIndex: 1,
    data: getDateMsgCntData("2023")
  },
  {
    type: 'heatmap',
    coordinateSystem: 'calendar',
    calendarIndex: 2,
    data: getDateMsgCntData("2024")
  }]
});
</script>

<template>
  <v-chart :option="calendar_heatmap_option" style="height: 500px; width: 1000px; margin-bottom: 100px;" />
</template>

<style scoped></style>
