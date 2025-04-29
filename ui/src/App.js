import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.scss';
import NodesPage from './components/NodesPage/NodesPage'
import NodePage from './components/NodePage/NodePage'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/node/:nodeId" element={<NodePage />}/>
        <Route path="/" element={<NodesPage />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
