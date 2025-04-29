import { IfxTable } from '@infineon/infineon-design-system-react';
import './nodesTable.scss';
import { useEffect, useState } from 'react';

function Table({ itemsPerPage }) {

  const [items, setItems] = useState([])

  useEffect(() => {

    async function fetchData() {
      try {
        const response = await fetch(`http://localhost:5000/api/ealite/configurations`);
        const result = await response.json();
        setItems(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  
    fetchData();
  }, []);


  if (!items.length) {
    return <div>Loading...</div>;
  } else {

    const tableHeaders = [
      {"headerName": "ID", "field":"id", "sortable":true,"sort":"desc", "unSortIcon":true},
      {"headerName": "Status", "field":"status", "sortable":true,"unSortIcon":true},
      {"headerName": "Description", "field":"description", "sortable":true},
      {"headerName": "",  "field": "button"}
    ];

    const tableRows = items.map((row) => {
      return {
        id: row.id,
        status: ["NETWORK READY", "OPERATIONAL READY", "OFF", "UPDATING", "DEFECT", "DISABLED"][Math.floor(Math.random() * 6)],
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod...",
        button: {
          disabled: false,
          variant: "primary",
          size: "s",
          target: "_self",
          href: `node/${row.id}`,
          theme: "default",
          type: "button",
          fullWidth: true,
          text: "Details"
        }
      };
    });

    console.log('tableRows:', JSON.stringify(tableRows));

    return (

      <IfxTable 
        row-height='default'
        cols={JSON.stringify(tableHeaders)}
        rows={JSON.stringify(tableRows)}
        table-height='auto'
        paginationPageSize={itemsPerPage}
        filterOrientation='none'>
      </IfxTable>
    );
  }

}

export default Table;
