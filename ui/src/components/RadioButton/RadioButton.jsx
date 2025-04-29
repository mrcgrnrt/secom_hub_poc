import { IfxRadioButton } from '@infineon/infineon-design-system-react';
import './radiobutton.scss';

function RadioButton( { error, disabled, checked, size, name, value }) {
  return (
  <IfxRadioButton error={error} disabled={disabled} checked={checked} size={size} name={name} value={value}>Text</IfxRadioButton>
  );
}

export default RadioButton;