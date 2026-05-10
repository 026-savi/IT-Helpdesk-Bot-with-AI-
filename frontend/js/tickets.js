let allTickets = [];

/* LOAD TICKETS */

async function loadTickets() {

    try {

        const response = await fetch("http://127.0.0.1:8001/tickets");

        const tickets = await response.json();

        allTickets = tickets;

        renderTickets(tickets);

    } catch (error) {

        console.error("Error loading tickets:", error);

    }

}

/* RENDER TICKETS */

function renderTickets(tickets) {

    const tableBody = document.getElementById("ticketTableBody");

    tableBody.innerHTML = "";

    /* IF NO RESULTS FOUND */

    if (tickets.length === 0) {

        tableBody.innerHTML = `

            <tr>
                <td colspan="4" style="
                    text-align:center;
                    padding:40px;
                    color:#94a3b8;
                    font-size:18px;
                ">
                    No tickets found
                </td>
            </tr>

        `;

        return;

    }

    /* SHOW TICKETS */

    tickets.forEach(ticket => {

        const row = document.createElement("tr");

        row.innerHTML = `

            <td>${ticket.id}</td>

            <td>${ticket.query}</td>

            <td>${ticket.status}</td>

            <td>${ticket.priority}</td>

        `;

        tableBody.appendChild(row);

    });

}

/* SEARCH FUNCTION */

document.getElementById("searchTicket").addEventListener("input", function () {

    const searchValue = this.value.trim().toLowerCase();

    /* IF SEARCH EMPTY */

    if (searchValue === "") {

        renderTickets(allTickets);

        return;

    }

    /* FILTER TICKETS */

    const filteredTickets = allTickets.filter(ticket =>

        ticket.query.toLowerCase().includes(searchValue) ||

        ticket.status.toLowerCase().includes(searchValue) ||

        ticket.priority.toLowerCase().includes(searchValue) ||

        String(ticket.id).includes(searchValue)

    );

    renderTickets(filteredTickets);

});

/* INITIAL LOAD */

loadTickets();