/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package matematica;

/**
 *
 * @author ferme
 */
public class Numeros {


        public boolean numeroPar(int n){
            return n%2==0;
            
        }
        
        public int  areaQuadrado( int lado){
            return lado*lado;
        }
        
        public boolean numeroDivisivel (int dividendo, int divisor){
                return dividendo%divisor==0;
        }
    
}
