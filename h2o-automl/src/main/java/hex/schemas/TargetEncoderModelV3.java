package hex.schemas;

import ai.h2o.automl.targetencoding.TargetEncoderModel;
import water.api.schemas3.ModelSchemaV3;

public class TargetEncoderModelV3 extends ModelSchemaV3<TargetEncoderModel, TargetEncoderModelV3, TargetEncoderModel.TargetEncoderParameters, TargetEncoderV3.TargetEncoderParametersV3,
        TargetEncoderModel.TargetEncoderOutput, TargetEncoderOutputV3> {

  @Override
  public TargetEncoderOutputV3 createOutputSchema() {
    return new TargetEncoderOutputV3();
  }

  @Override
  public TargetEncoderV3.TargetEncoderParametersV3 createParametersSchema() {
    return new TargetEncoderV3.TargetEncoderParametersV3();
  }
}
