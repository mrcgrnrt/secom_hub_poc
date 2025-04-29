import { IfxBasicTable } from '@infineon/infineon-design-system-react';
import './capTable.scss';
import { useEffect, useState } from 'react';

function Table({ nodeId }) {

  const [capabilities, setCapabilities] = useState([])

  useEffect(() => {

    async function fetchData() {
      try {
        const response = await fetch(`http://localhost:5000//api/ealite/decodedconfigurations/${nodeId}`);
        const result = await response.json();
        setCapabilities(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  
    fetchData();
  }, []);


  if (!capabilities.length) {
    return <div>Loading...</div>;
  } else {

    const tableHeaders = [
      {"headerName":"ConvType", "field":"conversionType", "sortable":true,"unSortIcon":true},
      {"headerName":"Model", "field":"model", "sortable":true},
      {"headerName":"OpType", "field":"operationsType", "sortable":true},
      {"headerName":"TS", "field":"timeseries", "sortable":true},
      {"headerName":"Type", "field":"type", "sortable":true},
      {"headerName":"VType", "field":"valueType", "sortable":true}
    ];

    const tableColumns = capabilities.map((row) => {
      return {
        conversionType: row.conversionType,
        model: row.model,
        operationsType: row.operationsType,
        timeseries: row.timeseries,
        type: row.type,
        valueType: row.valueType
      };
    });

    return (

      <IfxBasicTable 
        row-height='default'
        cols={JSON.stringify(tableHeaders)}
        rows={JSON.stringify(tableColumns)}
        table-height='auto'>
      </IfxBasicTable>
    );
  }

}

export default Table;
