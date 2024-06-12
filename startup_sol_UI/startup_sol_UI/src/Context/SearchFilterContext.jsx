import React, { useContext } from "react";
import { createContext } from "react";

import { FetchDataContext } from "../Context/FetchDataContext";
// import { PaginationContext } from "../Context/PaginationContext";

export const SearchFilterContext = createContext();

export function SearchFilter(props) {
  const {
    searchQuery,
    searchTarget,
    setDataFromAPI,
    isLoading,
    setIsLoading,
    dataFromAPI,
    masterSelected
  } = useContext(FetchDataContext);

  async function SearchOnAppliedFilter() {
    setIsLoading(true);
    const DATA_FORMAT = {
      query: searchQuery,

      target: searchTarget,
      filters: masterSelected
    };
    console.log(DATA_FORMAT);

    // const response = await fetch(process.env.REACT_APP_URL, {
    const response = await fetch("http://172.16.10.19:8877/lucene/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify(DATA_FORMAT)
    });
    const json = await response.json();
    // setTimeout(() => {
    //   setDataFromAPI(json);
    //   setIsLoading(false);
    // });
    setDataFromAPI(json);
    setIsLoading(false);
    console.log(json);
  }

  return (
    <SearchFilterContext.Provider
      value={{
        SearchOnAppliedFilter
      }}
    >
      {props.children}
    </SearchFilterContext.Provider>
  );
}
