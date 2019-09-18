/*
  Programa que mide la temperatura del ambiente a través de un sensor LM335 y envía la lectura mediante protocolo UART a la PC
  y a un dispositivo externo, en este caso, una Raspberry Pi. 
  En lugar de enviar la lectura a una Raspberry se puede enviar a cualquier otro dispositivo con conexión UART.

  En este caso la conexión UART entre el ESP32 y la PC se utiliza para debbuging
*/

const int sensor = 34; //Pin GPIO que va conectado al sensor LM335

void setup() 
{
  // -------------- Configuración UART --------------
  
  //Se crean los handlers para la comunicación serial
  // Formato: Baud_Rate, Protocolo, Pin_RX, Pin_TX

  //Comunicación con la PC
  Serial.begin(115200);  //RX, TX -> Cable USB
  
  //Comunicación con la Raspberry
  Serial2.begin(115200); // RX -> GPIO16 / TX -> GPIO17


  // -------------- Configuración ADC --------------
  
  // NOTA: La lectura del ADC tarda 433 [us] 
  
  analogReadResolution(12);       //Resolución de 12 bits. Rango del ADC entre 0 y 4095
  analogSetAttenuation(ADC_11db); //Establece la atenuación de ambos ADC a 11db en todos los canales
                                  /*Valores permitidos:  
                                     ADC_0db   -> Sin atenucación.    Lecturas de hasta 1.1 [V]
                                     ADC_2_5db -> Atenuación de 1.34. Lecturas de hasta 1.4 [V]
                                     ADC_6db   -> Atenuación de 1.5.  Lecturas de hasta 1.9 [V]
                                     ADC_11db  -> Atenuación de 3.6.  Lecturas de hasta 3.3 [V] */
}

void loop() 
{
  //Se realiza la lectura del ADC y conversión de temperatura
  float lecturaADC = analogRead(sensor);
  float tempKelvin = (lecturaADC * 330) / 4095;
  float tempCelsius = tempKelvin - 273.15;

  //Se envía la temperatura calculada a la PC
  Serial.println(tempCelsius); 

  //Se envían todos los datos a la Raspberry
  Serial2.print(lecturaADC);
  Serial2.print(",");
  Serial2.print(tempKelvin);
  Serial2.print(",");
  Serial2.println(tempCelsius);
  
  delay(1000);  //Retraso de 1000 [ms]
}
