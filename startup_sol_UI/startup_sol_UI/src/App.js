import "./App.css";
// import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/css/bootstrap.min.css";

import Screen from "./Containers/Screen/Screen";
import { FetchDataContextProvider } from "../src/Context/FetchDataContext";
import { SearchFilter } from "../src/Context/SearchFilterContext";

function App() {
  return (
    <div className="App">
      {/* FetchDataContextProvider  is responsible for fetching the data from the API and, 
      hence set it in the context, which then passes to different Components and Contexts. */}

      <FetchDataContextProvider>
        {/* SearchFilter is a Context which is responsible for fetching the filters data from the FetchDataContextProvider and, 
      hence set it in the context, which then passes to different Components and Contexts*. */}
        <SearchFilter>
          {/* Screen is the main component used for combining all the custom components together */}
          <Screen />
        </SearchFilter>
      </FetchDataContextProvider>
    </div>
  );
}

export default App;
