/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package matematica;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author ferme
 */
public class MatematicaTest {
    
    private Numeros n;
    
    public MatematicaTest() {
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }
    
    @Before
    public void setUp() {
        
        n = new Numeros();
    }
    
    @After
    public void tearDown() {
    }

    /**
     * Test of main method, of class Matematica.
     */
    @Test
    public void testNumeroPar() {
        assertTrue(n.numeroPar(8));
    }
    
    @Test
    public void testAreaQuadrada() {
        
        assertEquals(100, n.areaQuadrado(10));
    }
    @Test
    public void testDivisivel() {
        
        assertTrue(n.numeroDivisivel(4, 2));
    
    }
    
}
