import { IfxPagination } from '@infineon/infineon-design-system-react';
import './pagination.scss';

function Pagination( { total, currentPage, onIfxPageChange }) {
  return (
    <IfxPagination total={total} current-page={currentPage} onIfxPageChange={onIfxPageChange}></IfxPagination>
  );
}

export default Pagination;