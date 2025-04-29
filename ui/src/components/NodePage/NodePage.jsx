import React, { useState, useEffect } from 'react';
import { 
  IfxTextField
} from '@infineon/infineon-design-system-react';
import './nodePage.scss';
import TextField from '../TextField/TextField';
import Navbar from '../Navbar/Navbar';
import Table from './CapTable';

import { useParams } from 'react-router-dom';


function NodePage() {

  const { nodeId } = useParams();
  console.log('Node ID:', nodeId);

  const [node, setNode] = useState({
    id: '',
    description: '',
    status: 'OPERATIONAL READY',
    swVersion: '1.0.0',
    influx:{
      host: 'localhost',
      port: '8086',
      endpoint: '/api/v2'
    }
  });

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch(`http://localhost:5000/api/ealite/configurations/${nodeId}`);
        const result = await response.json();
        setNode({
          id: result.id || 'n.a.',
          description: 'Lirum ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
          status: result.status || 'OPERATIONAL READY',
          swVersion: result.swVersion || '1.0.0',
          influx: result.influx || {
            host: 'localhost',
            port: '8086',
            endpoint: '/api/v2'
          }
        });
        console.log('Node data:', result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  
    fetchData();
  }, []);

  return (
    <div className='container'>
      <div className="navbar__wrapper">
        <Navbar />
      </div>
      <div className="main__wizard-template-wrapper">

        <div className="content__wrapper">
          <div className="form__wrapper">
            <div className="tittle__wrapper">SECoM Node - {node.id}</div>
              <div className="section__wrapper">
                
                <div className="section">
                  <div className="section__title-wrapper">Info</div>
                  <div className="input__fields-wrapper">
                    <div className="text__fields-wrapper">
                      <div className="text__field">
                        <TextField label="ID" error="false" disabled="true" size="m" success="false" placeholder="ID" required="false" optional="false" name="text-field" show-delete-icon="false" value={node.id}/>
                      </div>
                      <div className="text__field">
                        <TextField label="SW Version" error="false" disabled="true" size="m" success="false" placeholder="SW Version" required="false" optional="false" name="text-field" show-delete-icon="false" value={node.swVersion} />
                      </div>
                    </div>
                    <div className="text__fields-wrapper">
                      <div className="text__field">
                        <TextField label="Status" error="false" disabled="true" size="m" success="false" placeholder="Status" required="false" optional="false" name="text-field" show-delete-icon="false" value={node.status} />  
                      </div>
                    </div>
                    <div className="text__fields-wrapper">
                      <div className="text__field">
                        <ifx-textarea label="Description" error="false" disabled="true" size="m" success="false" placeholder="Description" required="false" optional="false" name="text-field" full-witdh="true" show-delete-icon="false" value={node.description}  />  
                      </div>
                    </div>
                  </div>
                </div>

                <div className="section">
                  <div className="section__title-wrapper">Connection</div>
                  <div className="input__fields-wrapper">
                    <div className="text__fields-wrapper">
                      <div className="text__field">
                        <TextField label="Host" error="false" disabled="true" size="m" success="false" placeholder="Status" required="false" optional="false" name="text-field" show-delete-icon="false" value={node.influx.host} />  
                      </div>
                      <div className="text__field">
                        <TextField label="Port" error="false" disabled="true" size="m" success="false" placeholder="Status" required="false" optional="false" name="text-field" show-delete-icon="false" value={node.influx.port} />  
                      </div>
                    </div>
                    <div className="text__fields-wrapper">
                      <div className="text__field">
                        <TextField label="Endpoint" error="false" disabled="true" size="m" success="false" placeholder="Status" required="false" optional="false" name="text-field" show-delete-icon="false" value={node.influx.endpoint} />  
                      </div>
                    </div>
                    <div className="text__fields-wrapper">
                      <div className="text__field">
                        <TextField label="Token" error="false" disabled="true" size="m" success="false" placeholder="Status" required="false" optional="false" name="text-field" show-delete-icon="false" value={node.influx.token} />  
                      </div>
                    </div>
                  </div>
                </div>

                <div className="section">
                  <div className="section__title-wrapper">Capabilities</div>
                  <div className="tab-wrapper">
                    <Table nodeId={nodeId} />
                  </div>
                </div>

              </div>
            </div>
          </div>
        </div>
      </div>
  )
}

export default NodePage;

