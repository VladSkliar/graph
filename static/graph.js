function getData(){
$.ajax({
  method: "GET",
  dataType: "json",
  url: window.data_url,
  success: function(result){
        var data = []
        var chart_data = []
        var info = {}
        for(var i = 0; i<result.length; i++){
            info = {}
            info['label'] =result[i]['city']
            info['place'] = i + 1
            info['zipcode'] = result[i]['_id']
            info['value'] = result[i]['pop']
            data.push(info)
        }
        info = {}
        info['key'] = 'Popularity'
        info['values'] = data
        chart_data.push(info)
        buildGraph(chart_data)
    }
});
}
function buildGraph(data){
nv.addGraph(function() {
  var chart = nv.models.discreteBarChart()
    .x(function(d) { return d.place })
    .y(function(d) { return d.value })
    .staggerLabels(true)
    .tooltips(true)
    .showValues(false)



    chart.tooltip.contentGenerator(function (d) {
        return '<p><strong>' + d.data['label'] + '</strong></p>' +
           '<p>zipcode:' + d.data['zipcode'] + ' popularuty: ' + d.data['value'] + '</p>';
    })
    chart.yAxis
        .tickFormat(d3.format("d"));

  d3.select('#chart svg')
    .datum(data)
    .call(chart)
    ;
  nv.utils.windowResize(chart.update);

  return chart;
});
}
getData()
