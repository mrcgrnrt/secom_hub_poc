import Table from './NodesTable';
import Navbar from '../Navbar/Navbar';
import Pagination from '../Pagination/Pagination';
import './nodesPage.scss';
import { useEffect, useState } from 'react';

function NodesPage() {
  // const [currentPage, setCurrentPage] = useState(1)
  // const [itemsPerPage, setItemsPerPage] = useState(10)
  // const [totalRows, setTotalRows] = useState(10);

  // function handlePageChange(event) {
  //   setCurrentPage(event.detail.currentPage)
  //   setItemsPerPage(event.detail.itemsPerPage)
  // }

  // useEffect(() => {
  //   async function fetchData() {
  //     try {
  //       const response = await fetch(`http://localhost:5000/api/ealite/configurationsCount`);
  //       const result = await response.json();
  //       setTotalRows(result);
  //     } catch (error) {
  //       console.error('Error fetching data:', error);
  //     }
  //   }
  
  //   fetchData();
  // }, []);

  return (
    <div className='container'>
      <div className="navbar__wrapper">
        <Navbar />
      </div>
      <div className="main__table-template-wrapper">
        <div className="table__wrapper">
          <div className="table__desc">
            <h2>SECoM Nodes</h2>
            {/* <div className="pagination__wrapper">
              <Pagination total={totalRows} currentPage={1} onIfxPageChange={handlePageChange} />
            </div> */}
          </div>
          <Table itemsPerPage='10' />
        </div>
      </div>
    </div>
  )
}

export default NodesPage;
