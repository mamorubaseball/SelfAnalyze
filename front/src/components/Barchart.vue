<script>
import { Bar  } from 'vue-chartjs';

export default {
  extends: Bar,
  name: 'BarChart',
  props: ['chartData', 'options'],
  mounted () {
    console.log("this.data",this.chartData)
    this.renderChart(this.chartData, this.options)
  }
}
</script>