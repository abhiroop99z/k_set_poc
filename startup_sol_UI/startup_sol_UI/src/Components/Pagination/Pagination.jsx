import React, { useContext, useEffect, useState } from "react";

import { PaginationContext } from "../../Context/PaginationContext";
import { FetchDataContext } from "../../Context/FetchDataContext";

import styles from "./Pagination.module.css";

import ReactPaginate from "react-paginate";

function Paginations() {
  const {
    dataFromAPI
  } = useContext(FetchDataContext);
  const { setPostPerView } = useContext(PaginationContext);
  const [pageNumber, setPageNumber] = useState(0);

  const data = dataFromAPI["paper_res"];
  const count = data.length;
  const userPerPage = 10;
  const pagesVisited = pageNumber * userPerPage;
  const pageCount = Math.ceil(count / userPerPage);

  const pageChange = ({ selected }) => {
    setPageNumber(selected);
  };

  const displayData = data.slice(pagesVisited, pagesVisited + userPerPage);

  useEffect(() => {
    setPostPerView(displayData);
  }, [pageNumber]);

  return (
    <div>
      <ReactPaginate
        previousLabel={"prev"}
        nextLabel={"next"}
        pageCount={pageCount}
        onPageChange={pageChange}
        containerClassName={styles.paginationButtons}
        previousLinkClassName={"previousButton"}
        nextLinkClassName={"nextButton"}
        disabledClassName={styles.paginationDisabled}
        activeClassName={styles.paginationActive}
      ></ReactPaginate>
    </div>
  );
}

export default Paginations;
