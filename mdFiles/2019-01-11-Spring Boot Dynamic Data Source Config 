*2019-01-11*

# Spring Boot Dynamic Data Source Config Example

## application.properties
```
app.datasource.test1.url=jdbc:mysql://192.168.10.2:3306/test
app.datasource.test1.username=test
app.datasource.test1.password=1234

app.datasource.test2.url=jdbc:mysql://192.168.10.3:3306/test
app.datasource.test2.username=test
app.datasource.test2.password=1234

app.datasource.test3.url=jdbc:postgresql://192.168.10.4:5432/test
app.datasource.test3.username=test
app.datasource.test3.password=1234
```

## DataSourceConfig.java
```java
package me.test.config;

import java.util.HashMap;
import java.util.Map;

import org.springframework.boot.autoconfigure.jdbc.DataSourceProperties;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;

@Configuration
public class DataSourceConfig {
    public static Map<String, DataSourceProperties> dsproMap = new HashMap();

    @Primary
    @Bean(name="test1DSproper")
    @ConfigurationProperties("app.datasource.test1")
    public DataSourceProperties mzTestDataSourceProperties() {
        DataSourceProperties dspro = new DataSourceProperties();
        dsproMap.put("test1", dspro);
        return dspro;
    }
    
    @Bean(name="test2DSproper")
    @ConfigurationProperties("app.datasource.test2")
    public DataSourceProperties daTestDataSourceProperties() {
        DataSourceProperties dspro = new DataSourceProperties();
        dsproMap.put("test2", dspro);
        return dspro;
    }
    
    @Bean(name="test3DSproper")
    @ConfigurationProperties("app.datasource.test3")
    public DataSourceProperties mzDataSourceProperties() {
        DataSourceProperties dspro = new DataSourceProperties();
        dsproMap.put("test3", dspro);
        return dspro;
    }
   
}
```

## DBconn.java
```java
package me.test.db;

import java.util.HashMap;
import java.util.Map;

import javax.sql.DataSource;

import org.springframework.jdbc.core.JdbcTemplate;

import com.zaxxer.hikari.HikariDataSource;

import me.test.config.DataSourceConfig;

public class DBconn {
    static Map<String, DataSource> dsMap = new HashMap();
    static Map<String, JdbcTemplate> jtMap = new HashMap();
            
    public static JdbcTemplate getJdbcTemplate(String dataSourceName){
        if ( null == jtMap.get(dataSourceName)) {
            JdbcTemplate jt =  new JdbcTemplate(getDataSource(dataSourceName));
            jtMap.put(dataSourceName, jt);
            return jt;
        } else {
            return jtMap.get(dataSourceName);
        }
    }
    
    static DataSource getDataSource(String dataSourceName) {
        if (null == dsMap.get("dataSourceName")) {
            DataSource ds =  DataSourceConfig.dsproMap.get(dataSourceName)
                        .initializeDataSourceBuilder().type(HikariDataSource.class).build();
            dsMap.put(dataSourceName, ds);
            return ds;
        } else {
            return dsMap.get("dataSourceName");
        }
    }
    
}

```

## Test
```java
package me.test;

import java.util.List;
import java.util.Map;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import me.test.db.DBconn;

@RunWith(SpringRunner.class)
@SpringBootTest
public class DataSourceTest {
    @Autowired
    DBconn dbConn;
    
    @Test
    public void dynamicDataSource() {
        String sql = "select count(*) count from test.users";
        List<Map<String, Object>> list = dbConn.getJdbcTemplate("test1").queryForList(sql);
    }
}

```

