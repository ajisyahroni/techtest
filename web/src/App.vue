<script setup lang="ts">

import { ref } from 'vue';

// @ts-ignore
import TopTen from './data/best-top-ten-movies.json' // @ts-ignore
import GenresMarketShare from './data/genres-market-share.json'

const chartOptions = ref({
  labels: Object.keys(GenresMarketShare),
  chart: {
    id: 'df',
    width: '100%',

    type: "pie",
  },
  
  xaxis: {
    categories: Object.keys(GenresMarketShare),
  },
})
const series = ref(Object.values(GenresMarketShare))




</script>

<template>
  <v-app>
    <v-main>
      <v-sheet color="orange-lighten-5" height="100vh">
        <v-container fluid>
          <v-row>
            <v-col md="6" cols="12">
              <v-card title="Top Ten Movies All of the times">
                <v-table>
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>Title</th>
                      <th>Avg Rating</th>
                      <th>Viewers</th>
                    </tr>
                  </thead>

                  <tbody>
                    <tr v-for="movie in TopTen">
                      <td></td>
                      <td>{{ movie.title }}</td>
                      <td>{{ movie.avg_rating }}</td>
                      <td>{{ movie.jumlah_reviewer }}</td>
                    </tr>

                  </tbody>
                </v-table>
              </v-card>
            </v-col>

            <v-col md="6" cols="12">
              <v-card title="Genres Market Share">
                <apexchart :options="chartOptions" :series="series"></apexchart>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-sheet>
    </v-main>
  </v-app>
</template>

<style scoped >
table tr td:first-child::before {
  content: counter(row-num);
}

table tr {
  counter-increment: row-num;
}
</style>
