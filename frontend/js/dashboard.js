async function loadDashboard() {

    try {

        const response = await fetch("http://127.0.0.1:8001/stats");

        const data = await response.json();

        console.log(data);

        // Update values
        document.getElementById("totalTickets").innerText =
            data.total || data.total_tickets || 0;

        document.getElementById("resolvedTickets").innerText =
            data.resolved || data.resolved_tickets || 0;

        document.getElementById("openTickets").innerText =
            data.open || data.open_tickets || 0;

        document.getElementById("highTickets").innerText =
            data.high_priority || data.high_priority_tickets || 0;

    } catch (error) {

        console.error("Dashboard Error:", error);

    }

}

loadDashboard();