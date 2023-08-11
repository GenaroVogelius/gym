




console.log(llegadasData);
console.log(DAYS_LIST)

let isSaturday = 0;

function getDates(numb) {
  let currentDate = new Date()
  let currentDateToModify = new Date();
  var options = { weekday: "long", month: "short", day: "numeric" };
  let currentDateNumber = currentDateToModify.getDate();

  currentDateToModify.setDate(currentDateNumber - numb);
  

  if (currentDateToModify.toString().includes("Sun")) {
    currentDateToModify.setDate(currentDateNumber - numb - 1);
  }

    // ? si la fecha modifica incluye sabado y issabado es mayor que 2 y la fecha corriente no es sabado
    if (currentDateToModify.toString().includes("Sat") || isSaturday >= 2 && !currentDate.toString().includes("Sat"))  {
      isSaturday += 1;
      if (isSaturday >= 2) {
        currentDateToModify.setDate(currentDateNumber - numb + 1);
      }
    }

    console.log(currentDateToModify);
    let formattedDate = currentDateToModify.toLocaleDateString("es-ES", options);
    return formattedDate;
  }


// let todayNumber = todayAllDate.getDate(); 
// var yesterday = new Date(todayAllDate);
// console.log(todayNumber)
// todayAllDate.setDate(todayAllDate.getDate() - 1);

// console.log(yesterday);

// var options = { weekday: "long", month: "short", day: "numeric" };
// var formattedDate = todayAllDate.toLocaleDateString("es-ES", options);

// console.log(formattedDate);





HORARIOS = [
      "07:00",
      "07:30",
      "08:00",
      "08:30",
      "09:00",
      "09:30",
      "10:00",
      "10:30",
      "11:00",
      "11:30",
      "12:00",
      "12:30",
      "13:00",
      "13:30",
      "14:00",
      "14:30",
      "15:00",
      "15:30",
      "16:00",
      "16:30",
      "17:00",
      "17:30",
      "18:00",
      "18:30",
      "19:00",
      "19:30",
      "20:00",
      "20:30",
      "21:00",
    ];

const allValuesLists = [];

DAYS_LIST.forEach(day => {
  values_list = []
  HORARIOS.forEach(horario => {
    let cantidadPersonas = (llegadasData[day].time_counts[horario])
    if (cantidadPersonas === undefined) {
      values_list.push(0)
    }
    else {
      values_list.push(cantidadPersonas)
    }
  })

  allValuesLists.push(values_list);
});

console.log(allValuesLists)
const ctx1 = document.getElementById('myChart1')
const ctx2 = document.getElementById('myChart2')

    const TITLESIZE = 20
    const LABELSIZE = 15

    const colorBackground = [
      "rgba(255, 99, 132, 0.2)",
      "rgba(255, 205, 86, 0.2)",
      "rgba(75, 192, 192, 0.2)",
      "rgba(54, 162, 235, 0.2)",
      "rgba(153, 102, 255, 0.2)",
      "rgba(255, 159, 64, 0.2)",

      "rgba(0, 128, 0, 0.2)",
      "rgba(0, 0, 128, 0.2)",
      "rgba(201, 203, 207, 0.2)",
      "rgba(128, 0, 128, 0.2)",
    ];

const colorBorder = [
  "rgb(255, 99, 132)",
  "rgb(255, 205, 86)",
  "rgb(75, 192, 192)",
  "rgb(54, 162, 235)",
  "rgb(153, 102, 255)",
  "rgb(255, 159, 64)",

  "rgb(0, 128, 0)",
  "rgb(0, 0, 128)",
  "rgb(201, 203, 207)",
  "rgb(128, 0, 128)",
];

//       "Lunes","Martes","Miercoles","Jueves","Viernes","Sábado",

  const AsistenciaDia7 = allValuesLists[0]
  const AsistenciaDia6 = allValuesLists[1]
  const AsistenciaDia5 = allValuesLists[2]
  const AsistenciaDia4 = allValuesLists[3]
  const AsistenciaDia3 = allValuesLists[4]
  const AsistenciaDia2 = allValuesLists[5]
  const AsistenciaDia1 = allValuesLists[6]
  const AsistenciaDia0 = allValuesLists[7]
  
const generoData = [50, 60];

let configLineChart = {
  type: "line",
  data: {
    labels: HORARIOS,
    datasets: [
      {
        label: getDates(7),
        backgroundColor: colorBackground[0],
        borderColor: colorBorder[0],
        borderWidth: 2,
        data: AsistenciaDia7,
        fill: true,
      },
      {
        label: getDates(6),
        fill: true,
        backgroundColor: colorBackground[1],
        borderColor: colorBorder[1],
        borderWidth: 2,
        data: AsistenciaDia6,
      },
      {
        label: getDates(5),
        fill: true,
        backgroundColor: colorBackground[2],
        borderColor: colorBorder[2],
        borderWidth: 2,
        data: AsistenciaDia5,
      },
      {
        label: getDates(4),
        fill: true,
        backgroundColor: colorBackground[3],
        borderColor: colorBorder[3],
        borderWidth: 2,
        data: AsistenciaDia4,
      },
      {
        label: getDates(3),
        fill: true,
        backgroundColor: colorBackground[4],
        borderColor: colorBorder[4],
        borderWidth: 2,
        data: AsistenciaDia3,
      },
      {
        label: getDates(2),
        fill: true,
        backgroundColor: colorBackground[5],
        borderColor: colorBorder[5],
        borderWidth: 2,
        data: AsistenciaDia2,
      },
      {
        label: "Hoy",
        fill: true,
        backgroundColor: colorBackground[6],
        borderColor: colorBorder[6],
        borderWidth: 2,
        data: AsistenciaDia1,
      },
    ],
  },
  options: {
    plugins: {
      legend: {
        position: "top",
        labels: {
          font: {
            size: LABELSIZE,
          },
        },
      },
      title: {
        display: true,
        text: "Asistencias por día",
        font: {
          size: TITLESIZE,
        },
      },
    },
    // onHover: function (event, legendItem) {
    //   ctx1.style.cursor = "pointer";
    // },
    responsive: true,
    tooltips: {
      mode: "index",
      intersect: false,
    },
    hover: {
      mode: "nearest",
      intersect: true,
    },
    scales: {
      y: {
        ticks: {
          stepSize: 1, // Display only integer values
        },
      },
    },
  },
};



let configPieChart = {
    type: "pie",
    data: {
    labels: ['Masculino', 'Femenino',],
    datasets: [
      {
        data: generoData,
        backgroundColor: colorBackground,
        borderColor : colorBorder,
        borderWidth: 2,
      }
    ]
  },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "top",
          labels: {
            font: {
              size: LABELSIZE,
            },
          },
        },
        title: {
          display: true,
          text: "Asistencia Por Género",
          font: {
            size: TITLESIZE,
          },
        },
        tooltip: {
          callbacks: {
            label: function (context) {
              const label = configPieChart.data.labels[context.dataIndex];
              const value = generoData[context.dataIndex] || 0;
              const total = generoData.reduce((a, b) => a + b, 0);
              const percentage = ((value / total) * 100).toFixed(2);
              return `${label}: ${value} (${percentage}%)`;
            },
          },
        },
      },
    },
}
  

new Chart(ctx1, configLineChart)
new Chart(ctx2, configPieChart);


  // new Chart(ctx1, {
  //   type: "bar",
  //   data: AsistenciaData,
  //   options: {
  //     indexAxis: "y",
  //     responsive: true,
  //     plugins: {
  //       legend: {
  //         display: false,
  //       },
  //       title: {
  //         display: true,
  //         text: "División Etaria",
  //         font: {
  //           size: TITLESIZE,
  //         },
  //       },
  //       scales: {
  //         y: {
  //           beginAtZero: true,
  //         },
  //       },
  //     },
  //   },
  // });

// {
  //   type: 'line',
  //   data: AsistenciaData,
  //   options: {
  //   indexAxis: 'x',
  //     responsive: true,
  //     plugins: {
  //     legend: {
  //       display: false,
  //     },
  //     title: {
  //       display: true,
  //       text: 'División Etaria',
  //       font: {
  //         size: TITLESIZE,
  //       }
  //     },
  //     scales: {
  //       y: {
  //         beginAtZero: true,
  //       }
  //     }
  //   }
  // }});
