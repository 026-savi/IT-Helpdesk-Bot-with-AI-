async function loadAnalytics() {

    try {

        const response = await fetch("http://127.0.0.1:8001/tickets");

        const tickets = await response.json();

        const total = tickets.length;

        const resolved = tickets.filter(t => t.status === "resolved").length;

        const open = tickets.filter(t => t.status === "open").length;

        const high = tickets.filter(t => t.priority === "high").length;

        const medium = tickets.filter(t => t.priority === "medium").length;

        const low = tickets.filter(t => t.priority === "low").length;

        /* HERO */

        document.getElementById("analyticsTotal").innerText = total;

        document.getElementById("analyticsResolved").innerText = resolved;

        document.getElementById("analyticsOpen").innerText = open;

        document.getElementById("analyticsHigh").innerText = high;

        /* STATUS CHART */

        new Chart(document.getElementById("statusChart"), {

    type: "doughnut",

    data: {

        labels: ["Resolved", "Open"],

        datasets: [{

            data: [resolved, open],

            backgroundColor: [

                "#22c55e",
                "#f59e0b"

            ],

            borderWidth: 0

        }]

    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        cutout: "70%",

        plugins: {

            legend: {

                labels: {

                    color: "white",

                    font: {

                        size: 16

                    }

                }

            }

        }

    }

});

        /* PRIORITY CHART */

        new Chart(document.getElementById("priorityChart"), {

            type: "bar",

            data: {

                labels: ["High", "Medium", "Low"],

                datasets: [{

                    label: "Tickets",

                    data: [high, medium, low],

                    backgroundColor: [

                        "#ef4444",

                        "#facc15",

                        "#22c55e"

                    ],

                    borderRadius: 10

                }]

            },

            options: {

                responsive: true,

                scales: {

                    y: {

                        ticks: {

                            color: "white"

                        },

                        grid: {

                            color: "rgba(255,255,255,0.1)"

                        }

                    },

                    x: {

                        ticks: {

                            color: "white"

                        },

                        grid: {

                            display: false

                        }

                    }

                },

                plugins: {

                    legend: {

                        labels: {

                            color: "white"

                        }

                    }

                }

            }

        });

    } catch (error) {

        console.error(error);

    }

}

loadAnalytics();