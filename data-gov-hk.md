## 香港資料一線通
香港政府是有 open data 的網站[資料一線通](https://data.gov.hk/)，可供大眾免費使用。

## 數據集
雖然可以透過搜尋取得所需的 open data ，但經簡單查看後發現很多都難以直接採用，原因如下：
* 格式不一，PDF/XML/XLS/XLSX/JSON 也有
* 多為 Static file，JSON 也是整年的資料以 JSON 格式下載
* 缺乏說明文件，大多數沒有完整的說明文件去說明 open data 取得方式
* 只有部份有相關應用程式的 API 會定時更新及有說明文件

### 整理定時更新的 open data 類別(收集中）

#### 運輸
名稱 | 部門 | 檔案格式 | 更新頻率 | 說明
--- | --- | --- | --- | ---
[交通情況快拍圖像](https://data.gov.hk/tc-data/dataset/hk-td-tis_2-traffic-snapshot-images) | 運輸署 | JPEG/XML | 2分鐘 | 交通情況快拍圖像來自全港各主要道路上的183個閉路電視，讓你看到最新的交通情況。
[九龍東實時空置車位數目](https://data.gov.hk/tc-data/dataset/hk-devb-sps-sps) | 發展局 | JSON | 即時 | 起動九龍東辦事處現正邀請九龍東內停車場經營者開放實時空置車位數目及基本停車場資訊。
[實時空置車位資訊](https://data.gov.hk/tc-data/dataset/hk-devb-sps-sps) | 運輸署 | JSON | 即時 | 運輸署現正與停車場經營者合作，開放實時空置車位及基本停車場資訊，例如: 位置、 地址、高度限制等。
[實時空置車位資訊（整合版）](https://data.gov.hk/tc-data/dataset/hk-ogcio-st_div_04-carpark-info-vacancy) | 政府資訊科技總監辦公室 | JSON | 即時 | 此API服務整合由運輸署和起動九龍東辦事處所提供的實時空置車位數目及基本停車場資訊。
[抵港、離港船隻](https://data.gov.hk/tc-data/dataset/hk-md-mardep-vessel-arrivals-and-departures) | 海事處 | XML | 15分鐘 | 遠洋船隻抵港及離港的資料。
[特別交通消息](https://data.gov.hk/tc-data/dataset/hk-td-tis_1-special-traffic-news) | 運輸署 | XML | 有需要時 | 發生交通事故時，特別交通消息可讓你得知最新的特別行車及公共交通安排。
[行車時間顯示器](https://data.gov.hk/tc-data/dataset/hk-td-sm_2-journey-time-indicators) | 運輸署 | XML | 2分鐘 | 提供香港各主要道路(包括過海隧道)的平均行車時間。
[行車速度圖](https://data.gov.hk/tc-data/dataset/hk-td-sm_1-traffic-speed-map) | 運輸署 | XML | 2分鐘 | 提供香港各主要道路的平均行車速度。
[行車速度屏](https://data.gov.hk/tc-data/dataset/hk-td-sm_3-speed-map-panels) | 運輸署 | XML | 2分鐘 | 位於新界五個地點的行車速度屏的圖像，顯示主要幹道的行車狀況。
[香港水流預測](https://data.gov.hk/tc-data/dataset/hk-md-hydro-hong-kong-tidal-stream-prediction) | 海事處 | CSV | 每日 | 提供香港水域內11天預測的水流強度和流向，其中包括當天，未來8天及過去2天的預測結果。


## CKAN API
是由[資料一線通](https://data.gov.hk/)提供一套由 [CKAN](https://data.gov.hk/tc/developer/ckan-api) 開發的應用程式介面，以供開發者以程式訪問在[資料一線通](https://data.gov.hk/)上發布的公共資料的元數據。並提供英文/繁體中文/簡體中文的數據。雖然是完整的 API 架構，但除了[資料一線通 CKAN 應用程式介面開發指南](https://data-dot-one.gitbooks.io/ckan-api-development-guide/)外，沒有可以查看的 API 架構文件。
* 開發者需要先在 https://data.gov.hk/en-data/api/3/action/package_list 取得完整的數據列表
* 再以列表中的 `dataset id` 在 https://data.gov.hk/tc-data/api/3/action/package_show?id=[dataset_id] 中取得整個資料庫
* 或者先以政府服務分類在 https://data.gov.hk/tc-data/api/3/action/group_list 中尋找相應的服務分類 id
* 再在 https://data.gov.hk/tc-data/api/3/action/group_show?id=[group_id] 中以 `group id` 查看分類

暫時沒有相關文件可供查閱
