import React, {  useState } from "react";
import { createContext } from "react";
export const PaginationContext = createContext();

export function PaginationContextProvider(props) {

  const [postPerView, setPostPerView] = useState([]);

  return (
    <PaginationContext.Provider
      value={{
        postPerView,
        setPostPerView
      }}
    >
      {props.children}
    </PaginationContext.Provider>
  );
}
