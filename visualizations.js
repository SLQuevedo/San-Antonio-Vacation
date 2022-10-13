      var data = [
        {
          type: "indicator",
          mode: "gauge+number",
          value: wfreq,

          gauge: {
            axis: { range: [null, 9], ticks: 9},
            steps: [
              { range: [0, 1], color: "#e7fdeb"},
              { range: [1, 2], color: "#d1fbd8"},
              { range: [2, 3], color: "#a3ee5b"},
              { range: [3, 4], color: "#75DB66"},
              { range: [4, 5], color: "#66d855"},
              { range: [5, 6], color: "#53C027"},
              { range: [6, 7], color: "#40ba0f"},
              { range: [7, 8], color: "#2F8F19"},
              { range: [8, 9], color: "#188300"}
            ],
            threshold: {
              line: { color: "red", width: 3 },
              thickness: 0.75,
              value: wfreq

            }
          }
        }
      ];

      var gaugelayout = {
        title: "Belly Button Washing Frequency <br> Scrubs per Week",
        margin:  { t: 0, b: 0 },
        width: 600,
        height: 450
    };
      Plotly.newPlot('gauge', data, gaugelayout);