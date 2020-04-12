#
# export PYTHONPATH=.:ecoz2py
# python ecoz2_vq_learn_test.py
#
import ecoz2py as ecoz2

USE_WANDB = True

print("USE_WANDB: {}".format(USE_WANDB))

if USE_WANDB:
    import wandb

print("ECOZ2 C version: {}".format(ecoz2.get_version()))

codebook_class_name = 'F'

predictor_filenames = [
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10639.594_10642.075.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10651.289_10653.738.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10662.244_10664.453.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10672.805_10675.1045.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10683.31_10686.058.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10697.284_10699.585.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10711.357_10714.807.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10735.727_10737.598.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10758.276_10760.3125.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__11194.789_11197.028.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__11207.257_11209.98.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__11219.452_11221.176.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__11230.415_11232.402.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__11254.07_11256.843.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__11267.521_11270.192.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__11281.342_11283.494.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__11295.333_11297.568.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__11698.163_11700.872.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__11711.402_11713.595.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__11723.8545_11726.442.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__11736.308_11738.596.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__11748.033_11750.771.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__11760.243_11762.596.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1208.7683_1211.631.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12084.397_12086.683.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12094.822_12097.229.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12104.937_12107.039.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12134.222_12136.661.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12164.006_12166.043.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12178.1455_12180.007.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12192.308_12194.274.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12208.255_12210.268.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12223.81_12226.178.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12262.559_12264.467.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12274.526_12276.69.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12315.242_12317.679.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12342.307_12345.594.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12355.263_12358.591.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12371.422_12374.614.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12400.487_12402.454.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12414.302_12415.588.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1243.3508_1246.7445.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12720.133_12722.52.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1274.2628_1277.7025.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12743.615_12746.011.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12755.387_12757.385.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1286.8365_1288.8038.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1298.4506_1300.6254.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13034.694_13037.197.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13095.943_13098.758.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1310.107_1312.9822.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13137.898_13140.594.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1321.7654_1325.0897.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13458.936_13461.372.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13474.406_13477.305.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13489.318_13491.996.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13516.175_13519.079.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13528.399_13530.692.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13540.701_13543.439.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13552.533_13555.181.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1357.2444_1360.1492.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13805.574_13807.042.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1381.4652_1384.71.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13816.498_13818.646.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13838.649_13841.296.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13849.331_13851.678.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13859.756_13862.344.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13872.935_13875.582.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13884.706_13886.976.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13896.039_13898.738.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13907.417_13910.276.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13918.886_13921.385.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1393.6776_1397.0302.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__13930.173_13932.608.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__14267.823_14270.093.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__14283.453_14285.995.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1429.2528_1432.2372.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__14298.493_14301.05.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__14343.324_14345.987.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1440.8188_1444.2333.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1452.5695_1456.0093.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__14624.599_14627.068.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__14639.411_14642.317.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__14655.011_14657.465.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__14670.55_14673.259.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__14686.2705_14689.069.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__14702.657_14705.35.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__14717.121_14719.519.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__14728.983_14731.465.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15125.002_15127.589.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15140.087_15143.007.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15154.976_15157.669.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15169.591_15172.447.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15467.721_15470.46.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15482.655_15485.137.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15531.359_15533.417.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15542.858_15545.452.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15553.48_15555.795.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15564.783_15566.871.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15576.676_15579.205.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15835.85_15838.648.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15858.288_15861.012.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15869.53_15871.966.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15884.993_15887.49.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15917.6_15920.368.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15932.866_15935.401.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15945.561_15947.921.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15957.589_15960.615.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__16354.506_16356.715.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__16379.848_16382.405.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__16391.846_16394.531.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__16404.328_16407.129.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__16416.57_16419.082.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1962.8582_1965.6843.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1978.2794_1981.0168.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2007.9908_2011.4999.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2020.9602_2023.6755.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2033.593_2036.4788.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2046.0132_2048.5571.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2058.2256_2061.7346.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2070.0469_2072.729.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2081.8423_2085.4446.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2105.6208_2108.2979.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2116.6426_2120.2024.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2127.7139_2131.497.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2610.5303_2613.1853.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2627.7292_2630.1409.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2643.0122_2645.7363.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2658.5928_2661.3884.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2674.247_2677.0393.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2705.2053_2708.8582.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2720.2341_2723.7664.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2733.647_2737.3247.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3066.5674_3068.5642.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3091.6687_3094.126.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3106.3445_3109.7844.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3121.2644_3124.2603.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3135.3093_3138.7144.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3149.6594_3153.5874.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3163.6838_3167.592.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3178.7463_3182.5032.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3193.9312_3197.778.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3237.4497_3241.4187.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3253.3875_3256.8638.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3267.557_3271.1829.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3616.3518_3618.8542.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3632.331_3635.4766.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3647.1396_3649.1033.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3676.3662_3679.236.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3692.409_3695.4646.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3708.4087_3711.2944.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__371.56226_374.8239.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3725.2966_3727.6147.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3738.524_3740.1484.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3751.298_3753.5476.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__3777.0166_3779.7327.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__388.1481_391.1553.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__404.22507_407.55612.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4131.8364_4134.5347.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4142.641_4145.075.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4153.353_4156.791.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__416.624_419.14542.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4164.079_4166.513.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4174.416_4177.032.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4185.022_4187.853.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4199.9517_4202.3286.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4232.074_4235.187.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4261.3286_4263.895.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4275.3286_4278.458.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__428.58337_430.39114.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4289.1455_4291.894.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4304.641_4307.4063.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4720.916_4723.329.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4752.4272_4756.026.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4767.524_4770.939.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4780.9736_4784.6035.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4794.722_4798.9756.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__4836.6875_4840.3423.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5227.2314_5230.0127.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5243.0503_5245.65.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5274.4644_5276.3247.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5302.738_5304.9565.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5315.3213_5318.3013.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5327.812_5330.939.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5339.9136_5342.896.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5351.754_5354.138.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5363.218_5366.179.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5730.139_5732.811.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5744.8174_5747.9937.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5760.618_5763.235.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5774.8516_5777.293.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5807.9565_5810.9644.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5823.334_5826.278.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5837.631_5840.6387.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5852.5845_5855.6133.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5867.7285_5871.0073.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5881.3687_5885.372.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__6307.1646_6310.195.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__6321.503_6324.326.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__6336.355_6339.302.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__6362.714_6365.363.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__6374.8726_6377.5547.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__6386.297_6388.83.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__6397.9033_6400.801.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__6887.446_6890.3257.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__6901.214_6904.079.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__6916.2935_6919.173.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__6930.4126_6933.0703.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__6944.8647_6947.5303.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__6958.788_6961.3877.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__709.242_711.5511.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7154.6504_7156.2896.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7168.1694_7170.1396.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__724.94885_728.2789.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7259.668_7261.986.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7270.837_7273.389.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7295.95_7297.9043.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7312.2095_7313.981.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7355.296_7357.088.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7365.903_7368.1743.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7378.6616_7380.9136.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__739.0646_743.03534.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7422.0684_7424.486.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7436.9214_7439.4033.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7464.739_7467.595.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__751.16156_754.94763.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__763.928_767.22925.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7678.2964_7680.1177.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__776.0711_779.8572.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7806.2036_7808.5405.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7817.0996_7819.4673.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7827.465_7829.8823.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7838.277_7840.661.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7848.4595_7851.0425.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7873.4937_7875.9775.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7890.2646_7893.3555.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7905.4844_7907.479.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7920.1655_7922.827.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7932.9736_7935.3623.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7979.781_7982.276.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7991.3013_7994.046.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__8388.564_8390.719.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__8401.021_8403.223.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__8412.565_8414.563.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__8423.835_8425.855.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__8435.0205_8437.004.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__8445.785_8448.186.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__8457.148_8459.263.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__8468.177_8470.42.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__8479.129_8481.397.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__8824.473_8826.833.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__8842.523_8844.596.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__8891.031_8893.194.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__8946.257_8949.253.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9251.861_9253.778.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9272.828_9274.931.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9287.373_9289.249.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9301.277_9303.228.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9316.62_9318.667.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9328.315_9330.025.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9350.709_9352.581.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9758.322_9760.425.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9774.814_9777.054.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9791.882_9793.561.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9808.116_9810.099.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9824.775_9826.863.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9836.229_9837.836.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9848.378_9850.149.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9860.134_9862.296.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9871.602_9873.555.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9882.856_9884.827.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9893.95_9895.9375.prd',
  b'../ecoz2-whale/exerc01/data/predictors/TRAIN/F/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__9904.663_9906.997.prd',
]


if USE_WANDB:
    wandb.init(project="whale-vq")


def vq_learn_callback(variable, value):
    print("P: vq_learn_callback: variable={}, value={}".format(variable, value))
    if USE_WANDB:
        wandb.log({variable: value})


ecoz2.vq_learn(prediction_order=36,
               predictor_filenames=predictor_filenames,
               codebook_class_name=codebook_class_name,
               vq_learn_callback=vq_learn_callback)