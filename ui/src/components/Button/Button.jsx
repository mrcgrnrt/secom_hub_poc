import { IfxButton } from '@infineon/infineon-design-system-react';
import './button.scss';

function Button( { variant }) {
  return (
    <IfxButton type="button" disabled="false" variant={variant} size="m" target="_blank" theme="default"  full-width="false">
      Button 
    </IfxButton>
  );
}

export default Button;