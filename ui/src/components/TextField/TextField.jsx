import { IfxTextField } from '@infineon/infineon-design-system-react';
import './textfield.scss';

function TextField( { error, disabled, size, success, icon, placeholder, required, caption, optional, name, showDeleteIcon, value, label } ) {
  return (
    <IfxTextField error={error} disabled={disabled} size={size} icon={icon} success={success} placeholder={placeholder} caption={caption} required={required} optional={optional} name={name} show-delete-icon={showDeleteIcon} value={value}>{label}</IfxTextField>
  );
}

export default TextField;