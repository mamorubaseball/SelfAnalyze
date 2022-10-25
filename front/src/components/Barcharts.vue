<script>
import { Pie  } from 'vue-chartjs';
// import { Bar } from 'vue-chartjs/legacy';

export default {
  extends: Pie,
  name: 'BarCharts',
  props: ['chartData', 'options'],
  mounted () {
    console.log("this.data",this.chartData)
    this.renderChart(this.chartData, this.options)
  }
}
</script>