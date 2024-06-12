import React from "react";
import { createContext, useState } from "react";

export const FetchDataContext = createContext();

export function FetchDataContextProvider(props) {
  const [searchQuery, setSearchQuery] = useState("");
  const [searchTarget, setSearchTarget] = useState("");
  const [targetedDate, setTargetedDate] = useState();
  const [startDate, setStartDate] = useState();
  const [endDate, setEndDate] = useState(null);
  const [masterSelected, setMasterSelected] = useState([]);
  const [customerSelected, setCustomerSelected] = useState([]);
  const [verticalSelected, setVerticalSelected] = useState([]);
  const [typeOfService, setTypeOfService] = useState([]);
  const [regionSelected, setRegionSelected] = useState([]);
  const [isCustomerValue, setIsCustomerValue] = useState([]);
  const [isServiceValue, setIsServiceValue] = useState([]);
  const [isRegionValue, setIsRegionValue] = useState([]);
  const [isVerticalValue, setIsVerticalValue] = useState([]);

  const [isCheckValue, setIsCheckValue] = useState([]);

  const [dataFromAPI, setDataFromAPI] = useState();

  const [isLoading, setIsLoading] = useState(false);

  const [isResetFilter, setIsResetFilter] = useState();
  const [btnIsHighlighted, setBtnIsHighlighted] = useState(false);

  async function OnSubmit() {
    // setIsResetFilter(false);
    setIsLoading(true);
    setIsResetFilter(true);
    setCustomerSelected([]);
    setVerticalSelected([]);
    setRegionSelected([]);
    setTypeOfService([]);
    setIsCheckValue([]);
    setMasterSelected([])
    setTimeout(() => {
      setIsResetFilter(false);
    }, 1000);
    const jsonData = {
      query: searchQuery,
      target: searchTarget
      // target: "proposals"
    };
    console.log(jsonData);
    // const response = await fetch(process.env.REACT_APP_URL, {
    const response = await fetch("http://172.16.10.19:8877/lucene/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(jsonData)
    });
    const json = await response.json();
    console.log(json);
    // setIsResetFilter(true);
    // setTimeout(() => {
    //   setDataFromAPI(json);
    //   setIsLoading(false);
    // });
    setDataFromAPI(json);
    setIsLoading(false);
  }
  async function allTarget() {
    const response = await fetch("http://10.120.10.171:8020/lucene/target", {
      method: "POST",
      headers: {
        // "Content-Type": "application/json"
      }
    });
    const json = await response.json();
    console.log(json);
    return json;
  }

  return (
    <FetchDataContext.Provider
      value={{
        searchQuery,
        setSearchQuery,
        searchTarget,
        setSearchTarget,
        targetedDate,
        setTargetedDate,
        masterSelected,
        setMasterSelected,
        customerSelected,
        setCustomerSelected,
        verticalSelected,
        setVerticalSelected,
        regionSelected,
        setRegionSelected,
        typeOfService,
        setTypeOfService,
        dataFromAPI,
        setDataFromAPI,
        OnSubmit,
        startDate,
        setStartDate,
        endDate,
        setEndDate,
        isLoading,
        setIsLoading,
        isResetFilter,
        setIsResetFilter,
        isCustomerValue,
        setIsCustomerValue,
        isRegionValue,
        setIsRegionValue,
        isVerticalValue,
        setIsVerticalValue,
        isServiceValue,
        setIsServiceValue,
        btnIsHighlighted,
        setBtnIsHighlighted,
        isCheckValue,
        setIsCheckValue,
        allTarget
      }}
    >
      {props.children}
    </FetchDataContext.Provider>
  );
}
